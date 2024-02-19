import numpy as np
from typing import List
import hou
import nops_rand as nr

def Morph(kwargs : dict) -> None:

    node: hou.Node = kwargs['node']
    
    nodeshape: str = 'cop'

    node.setUserData('nodeshape',nodeshape)

    nprlist: List = nr.GetRandomList()

    color: hou.Color = hou.Color(nprlist)

    node.setColor(color) 
