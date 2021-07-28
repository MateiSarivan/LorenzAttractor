from lorat.lorat_simulation_gui import LoratGUI

def test_simulation_gui():
    gui = LoratGUI()
    assert gui.destroy_gui() == True