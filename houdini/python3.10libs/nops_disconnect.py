import nops_rand as nr
import nops_utils as nut
from PySide2.QtCore import QTimer
import time


def DisconnectWire(kwargs : dict) -> None:

    def CutWire() -> None:
        
        if node.isLockedHDA():
            
            node.allowEditingOfContents()
       
        node.setInput(0,None)

    def Lock() -> None:

        node.matchCurrentDefinition()    
    
    
    node: hou.Node = kwargs["node"]
    
    probability: float = nut.LoadDifficulty()    
    
    if nr.RandomTrigger(probability*0.1): #decreasing chances of happening as it becomes too annoying
        
        timer: QTimer = QTimer()
        
        timer.singleShot(int(3*300),CutWire)

        timer.singleShot(int(5*400),Lock)

        
        
     
    



