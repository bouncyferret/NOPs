import webbrowser
import time

def RickRoll() -> None:

    rick: string = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    now:float = time.time()
    
    if(int(now)%25==0):

        webbrowser.open(rick)
        
        
    return

    
