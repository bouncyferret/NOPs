import nops_rand as nr
import nops_utils as nut

def HideParms(kwargs:dict) -> None:

    node: hou.Node = kwargs['node']
    parms: tuple[hou.Parm] = node.parms()
    probability: float = nut.LoadDifficulty()
    
    for i,parm in enumerate(parms):

        if nr.RandomTrigger(probability,i):

            parm.hide(True)
            
            
        
    
