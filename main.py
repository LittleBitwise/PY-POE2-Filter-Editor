from nicegui import ui
from pprint import pp  # noqa
import json

ITEM_MODIFIERS = "./data/processed/item-modifiers.json"
ITEM_TYPES = "./data/processed/item-types.json"

# Item modifiers by Class
with open(ITEM_MODIFIERS) as file:
    item_modifiers: dict[str, dict[str, list[str]]] = json.load(file)

# Item types by Class or BaseType
with open(ITEM_TYPES) as file:
    item_types: dict[str, list[str]] = json.load(file)

ui.label("Add POE2 filter rule:")

# Tab layout
with ui.tabs() as tabs:
    byName = ui.tab("By name").tooltip("""
        This method is the most specific,
        especially useful for unique items, like Eye of Chayula
        """)
    byType = ui.tab("By base type").tooltip("""
        This method is useful when you want to filter a specific
        kind of item, like any items based on Gold Amulet or Vaal Gloves.
        This will include uniques of that type.
        """)
    byClass = ui.tab("By item class").tooltip("""
        This method is the most broad, useful especially if you
        want to hide items unusable by your build,
        or highlight general categories like Jewels or Rings.
        """)

# Tab content
with ui.tab_panels(tabs, value=byName):
    with ui.tab_panel(byName):
        with ui.row():
            ui.input("Item name")
            ui.checkbox("Partial match")
    with ui.tab_panel(byType):
        with ui.row():
            # Todo: Select doesn't allow partial inputs.
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
