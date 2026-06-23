import json

with open("poe-api-trade2-data-items.json") as file:
    # https://www.pathofexile.com/api/trade2/data/items
    data = json.load(file)

baseTypes = []

for category in data["result"]:
    for entry in category["entries"]:
        baseTypes.append(entry["type"])

with open("item-types.json", "w") as file:
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
