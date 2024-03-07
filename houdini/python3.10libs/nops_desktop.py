import random
from typing import Tuple, List
import hou
from time import sleep
import nops_rand as nra
import nops_utils as nut

def ShufflePanes(pane_tabs: Tuple[hou.PaneTab]):
    # BUG python panel "ConstraintBrowser" causes issues
    # BUG sometimes I get hou.PathPaneTab or hou.Pane hou.ObjectWasDeleted errors
    original_tabs: List[Tuple[hou.paneTabType, str, hou.PythonPanelInterface]] = []
    for i, tab in enumerate(pane_tabs):
        try:
            pane_path: str | None = tab.pwd().path()
        except AttributeError:
            pane_path = None
        tab_type = tab.type()
        if tab_type == hou.paneTabType.PythonPanel:
            original_tabs.append((tab.type(), pane_path, tab.activeInterface()))
        else:
            original_tabs.append((tab.type(), pane_path, None))

    random.shuffle(original_tabs)
    for i, tab in enumerate(pane_tabs):
        original_type = original_tabs[i][0]
        if original_type == hou.paneTabType.PythonPanel:
            new_tab: hou.paneTabType.PythonPanel = tab.setType(original_type)
            new_tab.setActiveInterface(original_tabs[i][2])
        else:
            try:
                tab.setType(original_type)
            except hou.ObjectWasDeleted:
                print(f"Failed to -> {original_type} ")  # DEBUG PRINT
                continue
        sleep(0.03)  # feels a bit better, might remove

        # TODO restore location of original (some panes dont have a /location/)
        # might not be needed, keeping it chaotic
        # tab.cd(original_tabs[i][1])


def ShuffleVisiblePanes():
    pane_tabs = hou.ui.currentPaneTabs()
    ShufflePanes(pane_tabs)


def ShuffleAllPanes():
    pane_tabs = hou.ui.paneTabs()
    ShufflePanes(pane_tabs)

def ResetToStartDesktop() -> None:

    difficulty: float = nut.LoadDifficulty() * 0.025

    if nra.RandomTrigger(difficulty):
        hou.hscript("desk set NOPS")
