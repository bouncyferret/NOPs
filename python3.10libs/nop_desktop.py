import random
from typing import Tuple, List
import hou


def shuffle_panes(pane_tabs: Tuple[hou.PaneTab]):
    original_tabs: List[Tuple[hou.paneTabType, str]] = []
    for i, tab in enumerate(pane_tabs):
        try:
            location = tab.pwd()
        except AttributeError:
            location = None
        original_tabs.append((tab.type(), location))

    random.shuffle(original_tabs)
    for i, tab in enumerate(pane_tabs):
        print("swapping", tab)  # debug print
        tab.setType(original_tabs[i][0])
        # TODO:
        # restore location of original (some panes dont have a /location/)
        # might not be needed, keeping it chaotic
        # tab.cd(original_tabs[i][1])


def shuffle_visible_panes():
    pane_tabs = hou.ui.currentPaneTabs()
    shuffle_panes(pane_tabs)


def shuffle_all_panes():
    pane_tabs = hou.ui.paneTabs()
    shuffle_panes(pane_tabs)
