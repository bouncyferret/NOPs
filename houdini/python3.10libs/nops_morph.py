import numpy as np
from typing import List
import hou
import nops_rand as nr
import nops_utils as nut

def Morph(kwargs : dict) -> None:

    node: hou.Node = kwargs['node']
    
    nodeshapes: tuple[str] = ('cop','_wbt_tux','_wbt_helix','_wbt_rustacean','_wbt_mustacheB')

    difficulty_index: int = nut.LoadDifficultyIndex()

    nodeshapes_slice: list[str] = list(nodeshapes)[:len(nodeshapes)-difficulty_index]

    nodeshape: str = nodeshapes_slice[nr.ChooseFromStringArray(nodeshapes_slice)]

    node.setUserData('nodeshape',nodeshape)

    nprlist: List = nr.GetRandomList()

    color: hou.Color = hou.Color(nprlist)

    node.setColor(color) 