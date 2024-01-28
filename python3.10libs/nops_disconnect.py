import random
from PySide2.QtCore import QTimer
import time

def DisconnectWire(kwargs : dict) -> None:
    
    node = kwargs["node"]
    id: int = node.sessionId()
    random.seed(id+int(time.time()))
    rng: int = random.randint(1,100)
    #probability could be driven by env var
    #user chooses difficulty
    #harder == higher chance of happening
    probability: int = 3
    if rng%probability==0:
        print("triggered")
        timer: QTimer = QTimer()
        timer.singleShot(int(3*300),lambda: node.setInput(0,None))
        timer.start()
        
     
    



