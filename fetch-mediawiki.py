from mediawiki import MediaWiki
from bs4 import BeautifulSoup
from pprint import pp  # noqa
import json
from pathlib import Path
import urllib.parse


def pathSafeString(url: str) -> str:
    return urllib.parse.quote(url, safe="")


poe2wiki = MediaWiki(url="https://www.poe2wiki.net/api.php")
poe2wiki.user_agent = "just-fetching-modifiers-im-sorry"
poe2wiki.use_cache = True


def localCache(title: str):
    # Page titles may contain slashes...
    path = f"webcache/{pathSafeString(title)}.html"
    path = Path(path)
    if path.is_file():
        with open(path) as file:
            print("HTML from local")
            return file.read()
    # Page not read before, fetch it
    page = poe2wiki.page(title)
    with open(path, "w") as file:
        file.write(page.html)
    print("HTML from HTTP")
    return page.html


def parse(html: str) -> dict[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    modifiers = {}
    # fmt: off
    for group in soup.select(".mod-compat__type-list"):
        em = group.find("em")
        if not em: continue
        label = em.text.strip()  # eg. "#% increased maximum Life"
        modifiers[label] = []
        for row in group.select("tr")[1:]:  # Skip header row
            col = row.find("td")
            if not col: continue
            modifiers[label].append(col.text.strip())  # Athlete's
    # fmt: on
    return modifiers


with open("item-modifiers.json", "w") as file:
    # fmt: off
    modifiers = parse(localCache("List of modifiers for body armours (strength)")) |\
        parse(localCache("List of modifiers for body armours (dexterity)")) |\
        parse(localCache("List of modifiers for body armours (intelligence)")) |\
        parse(localCache("List of modifiers for body armours (strength/intelligence)")) |\
        parse(localCache("List of modifiers for body armours (strength/dexterity)")) |\
        parse(localCache("List of modifiers for body armours (dexterity/intelligence)")) |\
        parse(localCache("List of modifiers for body armours (strength/dexterity/intelligence)"))
    # fmt: on

    output = {
        # Accessories
        "Amulets": parse(localCache("List of modifiers for amulets")),
        "Belts": parse(localCache("List of modifiers for belts")),
        "Quivers": parse(localCache("List of modifiers for quivers")),
        "Rings": parse(localCache("List of modifiers for rings")),
        "Body Armours": modifiers,
    }
    json.dump(output, file)
