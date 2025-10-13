import hou
import csv
import os
import json
from hutil.PySide import QtCore
from typing import Callable, Dict, Any
from nops_constants import Category, Context

class TimeWizard(QtCore.QTimer):

    def __init__(self, parent=None):
        super().__init__(parent)
        


def LoadDifficulty() -> float:

        match LoadDifficultyIndex():

            case 0:
                return .1
            case 1:
                return .25
            case 2:
                return .6
            case 3:
                return .9
        

def LoadDifficultyIndex() -> int:         

    
    nops_path: str = hou.getenv("NOPS")
    prefs_path: str = os.path.join(nops_path,"nops_prefs.json")
    difficulty_index: int = 0
    with open(prefs_path,'r') as file:

        prefs_dict: dict = json.load(file)
        
        difficulty_index = prefs_dict["difficulty"]

    return difficulty_index

    


def ScheduleFunction(delay: float, func: Callable) -> None:
    """
    Schedule a function to be executed after a specified delay.

    Args:
        func (callable): The function to be executed.
        delay (float, optional): The delay in seconds before executing the function. Defaults to 5.

    Returns:
        None
    """
    timer = TimeWizard(hou.qt.mainWindow())
    timer.singleShot(int(delay * 1000), func)


def TemporaryMessage(message: str, duration: float = 4, severity: int = 0) -> None:
    """
    Display a temporary message in the Houdini status bar.

    Args:
        message (str): The message to display.
        duration (int, optional): The duration of the message in seconds. Defaults to 4.
        severity (int, optional): The severity level of the message.
            0 - Message (default)
            1 - Warning
            2 - Error

    Returns:
        None
    """
    if severity == 0:
        hou.ui.setStatusMessage(message, severity=hou.severityType.Message)
    elif severity == 1:
        hou.ui.setStatusMessage(message, severity=hou.severityType.Warning)
    elif severity == 2:
        hou.ui.setStatusMessage(message, severity=hou.severityType.Error)

    ScheduleFunction(duration, lambda: hou.ui.setStatusMessage(""))


def CategoryToContext(cat: str) -> str:
    """
    This is dumb as hell ...
    This is so awful lol
    """
    match cat:
        case Category.OBJ.value:
            return Context.OBJ.value
        
        case Category.SOP.value:
            return Context.SOPS.value

        case Category.CHOP.value:
            return Context.CHOPS.value

        case Category.VOP.value:
            return Context.VOPS.value

        case Category.SHOP.value:
            return Context.SHOPS.value

        case Category.COP2.value:
            return Context.COPS2.value

        case Category.COP.value:
            return Context.COPS.value

        case Category.DOP.value:
            return Context.DOPS.value

        case Category.TOP.value:
            return Context.TOPS.value

        case Category.ROP.value:
            return Context.ROPS.value

        case Category.LOP.value:
            return Context.LOPS.value

        case _:
            return "unknown"


def GetBannedNodes() -> list[str]:
    basepath: str = hou.getenv("NOPS")
    list_banned_nodes: list[str] = []
    if basepath is not None :

        path_to_csv: str = os.path.join(
            basepath,
            "csvs/nodes_to_destroy.csv"
        )
    
        with open(path_to_csv,newline='')as csvfile:
            reader: csv.Reader = csv.reader(csvfile)
            list_banned_nodes: List[str] = [row[0] for row in reader]
    return list_banned_nodes

def IsBannedNode(node: hou.Node) -> bool:
    return node.type().name() in GetBannedNodes()

