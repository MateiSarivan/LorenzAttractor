from lorat.lorat_explorer_gui import LoratExplorerGUI

def test_explorer_gui():
    gui = LoratExplorerGUI()
    assert gui.destroy_gui() == True