from lorat.lorat_simulation_gui import LoratGUI
from lorat.lorat_explorer_gui import LoratExplorerGUI


def lorat_simulation():
    lorat = LoratGUI()
    lorat.run_gui()

def lorat_explorer():
    lorat = LoratExplorerGUI()
    lorat.run_gui()
