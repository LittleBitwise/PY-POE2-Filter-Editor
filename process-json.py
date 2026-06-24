import json

# https://www.pathofexile.com/api/trade2/data/items
POE2_ITEMS = "./data/raw/poe-api-trade2-data-items.json"
OUTPUT_ITEM_TYPES = "./data/processed/item-types.json"

with open(POE2_ITEMS) as file:
    data = json.load(file)

baseTypes = []

for category in data["result"]:
    for entry in category["entries"]:
        baseTypes.append(entry["type"])

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
        "BaseType": baseTypes,
    }
    json.dump(output, file)
