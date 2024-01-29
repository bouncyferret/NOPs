import hou
from PySide2.QtCore import QTimer
from typing import Callable, Dict, Any
import toml


def LoadConfig() -> Dict[str, Any] | None:
    """
    Load nops_config.toml as a dict :)

    Returns:
        Dict
        None - if missing $NOPS
    """
    configPath = hou.getenv("NOPS", None)
    if not configPath:
        return None

    with open(f"{configPath}/nops_config.toml") as file:
        return toml.loads(file.read())


def ScheduleFunction(delay: float, func: Callable) -> None:
    """
    Schedule a function to be executed after a specified delay.

    Args:
        func (callable): The function to be executed.
        delay (float, optional): The delay in seconds before executing the function. Defaults to 5.

    Returns:
        None
    """
    timer = QTimer(hou.qt.mainWindow())
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
