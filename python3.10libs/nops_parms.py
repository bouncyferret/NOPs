import nops_rand as nr

def HideParms(kwargs:dict) -> None:

    node: hou.Node = kwargs['node']
    parms: tuple[hou.Parm] = node.parms()

    for i,parm in enumerate(parms):

        if nr.RandomTrigger(0.9,i):

            parm.hide(True)
            
            
        
    
