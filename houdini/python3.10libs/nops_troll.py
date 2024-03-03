import webbrowser
import time
import nops_rand as nr
import hou

def RickRoll() -> None:

    rick: string = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    if nr.RandomTrigger(probability = 0.0002):

        webbrowser.open(rick)
        
        
    return

def OphideNode(node: hou.Node) -> None:

    if not node.type().hidden():

        category_name: str = node.type().category().name()
        hou.hscript(f"ophide {category_name} {node.type().name()}")
        

           
