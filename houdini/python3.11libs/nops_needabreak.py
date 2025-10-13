import hou
import nops_rand as nr
import nops_utils as nut
from sys import platform
from typing import List

def AnnoyingCook() -> None:

    hard: float = nut.LoadDifficulty() * 0.25
    
    if not nr.RandomTrigger(hard):
        
        return 
    
    lazymessages: List[str] = ["I need a break, go get a coffee or something...",
                               "Stuck in traffic...",
                               "Why don't YOU cook for once ?!",
                               "On my day off ?? Fine...",
                               "Call me Chefdini the way I be cooking!",
                               "Time to tell you about our lord and saviour PDG",
                               "Maybe close some tabs...",
                               "You could say 'Please' once in while :'("
                              ]
    
    if "linux" in platform:

        lazymessages.append("Having a chat with Tux")
        lazymessages.append("Admiring your OS")
    
    elif "darwin" in platform:

        lazymessages.append("Connecting Icook to your Iwatch")
        lazymessages.append("You're not using a trackpad are you ??")

    else: #user is on windows, how sad

        lazymessages.append("Fighting Windows for ressources...")
        lazymessages.append("So much bloat on your machine...")
                    
    lazymessage: str = lazymessages[nr.ChooseFromStringArray(lazymessages,slow=2)]
    
    with hou.InterruptableOperation(lazymessage,open_interrupt_dialog=True) as operation:

        # garbage operations that take time

        for i in range(15 + nut.LoadDifficultyIndex()*2):
            
            for j in range(10000):

                for k in range(1000):

                    lol: int  = j + k

            percent = float(i) / float(10)
            operation.updateProgress(percent)


            
    
