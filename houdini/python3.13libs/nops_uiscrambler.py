import hou
import nops_rand as nr
from enum import StrEnum
from typing import List

class NopsUiThemes(StrEnum):
    Pink = "Pinky Pie"
    Horrible = "Eyeburn"
    TooDark = "Invader"

    @staticmethod
    def themes() -> List[str]:
        return [theme.value for theme in NopsUiThemes]



def SetRandomColorTheme() -> None:

    if not hou.isUIAvailable():
        return

    themes: List[str] = NopsUiThemes.themes()
    index: int = nr.ChooseFromStringArray(themes)
    hou.ui.setApplicationTheme(themes[index])
