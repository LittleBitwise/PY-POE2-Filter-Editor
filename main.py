from nicegui import ui
from pprint import pp  # noqa
import json

ITEM_MODIFIERS = "./data/processed/item-modifiers.json"
ITEM_TYPES = "./data/processed/item-types.json"

with open(ITEM_MODIFIERS) as file:
    item_modifiers = json.load(file)

with open(ITEM_TYPES) as file:
    item_types = json.load(file)

ui.label("Add POE2 filter rule:")

# Tab layout
with ui.tabs() as tabs:
    byName = ui.tab("By name")  # "Eye of Chayula"
    byType = ui.tab("By base type")  # "Gold Amulet", "Vaal Gloves"
    byClass = ui.tab("By item class")  # "Amulets", "Gloves"

# Tab content
with ui.tab_panels(tabs, value=byName):
    with ui.tab_panel(byName):
        with ui.row():
            ui.input("Item name")
            ui.checkbox("Partial match")
    with ui.tab_panel(byType):
        with ui.row():
            # Todo: Would partial match conflict with select filter?
            ui.input("Base type")
            ui.checkbox("Partial match")
    with ui.tab_panel(byClass):
        with ui.row():
            ui.select(item_types["Class"], with_input=True)


# Todo: stats, amulet modifiers for now


@ui.refreshable
def statTierButtons() -> None:
    if not statSelect.value:
        return
    x: list = item_modifiers["Amulets"][statSelect.value]
    tiers = len(x)
    with ui.button_group().bind_visibility_from(statSelect, "value"):
        for i in range(tiers, 0, -1):
            ui.button(f"T{i}")


statSelect = ui.select(
    list(item_modifiers["Amulets"].keys()),
    with_input=True,
    on_change=lambda e: statTierButtons.refresh(),
)

statTierButtons()

with ui.button_group():
    ui.button("Hide")
    ui.button("Show")


ui.run()
