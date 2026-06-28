import json
from collections import Counter
import string

# https://www.pathofexile.com/api/trade2/data/items
POE2_ITEMS = "./data/raw/poe-api-trade2-data-items.json"
OUTPUT_ITEM_TYPES = "./data/processed/item-types.json"

with open(POE2_ITEMS) as file:
    data = json.load(file)

baseTypes = set()

for category in data["result"]:
    if category["label"] == "Gems":
        baseTypes.add("Uncut Skill Gem")
        baseTypes.add("Uncut Spirit Gem")
        baseTypes.add("Uncut Support Gem")
        continue  # Only uncut gems can drop.
    for entry in category["entries"]:
        baseTypes.add(entry["type"])


def sharedWords(strings):
    invalidGroups = ["of", "on", "the", "i", "ii", "iii"]
    counts = Counter()
    for s in strings:
        removePunctuation = str.maketrans("", "", string.punctuation)
        removeDigits = str.maketrans("", "", string.digits)
        words = s.translate(removePunctuation).translate(removeDigits).split()
        words = [w for w in words if w.lower() not in invalidGroups]
        counts.update(words)
    words = [word for word, count in counts.items() if count > 1]
    words.sort()
    return words


with open(OUTPUT_ITEM_TYPES, "w") as file:
    output = {
        "Class": [  # https://www.poe2wiki.net/wiki/Item_class
            "Amulets",
            "Augments",
            "Belts",
            "Body Armours",
            "Boots",
            "Bows",
            "Charms",
            "Crossbows",
            "Expedition Logbooks",
            "Flasks",
            "Foci",
            "Gloves",
            "Helmets",
            "Jewels",
            "Map Fragments",
            "Omens",
            "Pinnacle Keys",
            "Quarterstaves",
            "Quivers",
            "Relics",
            "Rings",
            "Sceptres",
            "Shields",
            "Bucklers",
            "Targes",
            "Tower Shields",
            "Skill Gems",
            "Spirit Gems",
            "Stackable Currency",
            "Staves",
            "Support Gems",
            "Tablets",
            "Two Hand Maces",
            "Wands",
            "Waystones",
        ],
        "BaseTypeGroup": sharedWords(baseTypes),
        "BaseType": list(baseTypes),
    }
    json.dump(output, file)
