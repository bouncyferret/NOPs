import hou
from PySide2.QtCore import QTimer


def temporaryMessage(message, duration=4, severity=0):
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
    timer = QTimer()
    timer.singleShot(duration * 1000, lambda: hou.ui.setStatusMessage(""))
    timer.start()


# TODO This function is has not been tested.
def scheduleFunction(func, delay=5):
    """
    Schedule a function to be executed after a specified delay.

    Args:
        func (callable): The function to be executed.
        delay (float, optional): The delay in seconds before executing the function. Defaults to 5.

    Returns:
        None
    """
    timer = QTimer()
    timer.singleShot(int(delay * 1000), func)
    timer.start()
