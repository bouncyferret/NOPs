import numpy as np
from typing import List
import hou

def Morph(kwargs : dict) -> None:

    node: hou.Node = kwargs['node']
    
    nodeshape: str = 'cop'

    node.setUserData('nodeshape',nodeshape)

    nprlist: List = np.random.default_rng(seed=node.sessionId()).random((3,)).tolist()

    color: hou.Color = hou.Color(nprlist)

    node.setColor(color) 
