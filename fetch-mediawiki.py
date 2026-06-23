from mediawiki import MediaWiki
from bs4 import BeautifulSoup
from pprint import pp  # noqa
import json

poe2wiki = MediaWiki(url="https://www.poe2wiki.net/api.php")
poe2wiki.user_agent = "just-fetching-modifiers-im-sorry"
poe2wiki.use_cache = True


def localCache(title: str, output: str):
    page = poe2wiki.page(title)
    with open(output, "w") as file:
        file.write(page.html)


def parse(html: str):
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


# https://www.poe2wiki.net/wiki/List_of_modifiers_for_amulets
# localCache("List of modifiers for amulets", "mediawiki.html")
# html = open("mediawiki.html")

html = poe2wiki.page("List of modifiers for amulets").html
modifiers = parse(html)

with open("item-modifiers.json", "w") as file:
    output = {"Amulet": modifiers}
    json.dump(output, file)
