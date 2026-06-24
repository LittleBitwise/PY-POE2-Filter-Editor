from nicegui import ui
from pprint import pp  # noqa
import json

ITEM_MODIFIERS = "./data/processed/item-modifiers.json"

ui.label("Add POE2 filter rule:")

# Tab layout
with ui.tabs() as tabs:
    byName = ui.tab("By name")
    byType = ui.tab("By type")

# Tab content
with ui.tab_panels(tabs, value=byName):
    with ui.tab_panel(byName):
        with ui.row():
            ui.input("Item name")
            ui.checkbox("Partial match")
    with ui.tab_panel(byType):
        with ui.row():
            ui.input("Base type")
            ui.checkbox("Partial match")


# Todo: stats, amulet modifiers for now
with open(ITEM_MODIFIERS) as file:
    data = json.load(file)


@ui.refreshable
def statTierButtons() -> None:
    if not statSelect.value:
        return
    x: list = data["Amulets"][statSelect.value]
    tiers = len(x)
    with ui.button_group().bind_visibility_from(statSelect, "value"):
        for i in range(tiers, 0, -1):
            ui.button(f"T{i}")


statSelect = ui.select(
    options=list(data["Amulets"].keys()),
    with_input=True,
    on_change=lambda e: statTierButtons.refresh(),
)

statTierButtons()

with ui.button_group():
    ui.button("Hide")
    ui.button("Show")


ui.run()
