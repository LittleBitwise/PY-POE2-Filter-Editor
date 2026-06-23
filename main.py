from nicegui import ui

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

with ui.button_group():
    ui.button("Hide")
    ui.button("Show")


ui.run()
