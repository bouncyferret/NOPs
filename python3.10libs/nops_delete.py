def delete_node(kwargs) -> None:
    # this function displays an image and destroys node if node is listed in the destroyables
    import csv
    import os
    import hou
    import time
    from PySide2.QtCore import QTimer
    from typing import Callable,Tuple,List

    def AddBackgroundImage() -> None:

        editor: hou.NetworkEditor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

        editor.setBackgroundImages([])
        
        b_img: List[hou.NetworkImage] = [img for img in editor.backgroundImages()]

        img: hou.NetworkImage = hou.NetworkImage()   
            
        size: hou.Vector2 = node.size()
        
        img.setRect(hou.BoundingRect(2,2,size[0],size[1]))
        
        img.setRelativeToPath(node.path())  
                                                        
        img.setPath('$SIDEFXLABS/misc/stickers/Emoji/SIDEFX_CUSTOM_EMBLEMS 08.png')
                    
        b_img.append(img) 

        editor.setBackgroundImages(b_img)
        

    def KillNode() -> None:
        
        kwargs['node'].destroy()

    def LaunchTimer(interval: int , fun: Callable ) -> None:

        timer: QTimer = QTimer()
        timer.singleShot(int(interval*500),fun)
        timer.start()

    
    node: hou.Node = kwargs['node']
    list_banned_nodes: List[str] = list()
    basepath: str = hou.getenv("NOPS")
    
    
    if basepath is not None :

        path_to_csv: str = os.path.join(basepath,"csvs/nodes_to_destroy.csv")
        
        with open(path_to_csv,newline='')as csvfile:
            reader: csv.Reader = csv.reader(csvfile)
            list_banned_nodes: List[str] = [row[0] for row in reader]
        
        if node.type().name() in list_banned_nodes:
            
            LaunchTimer(2,AddBackgroundImage)
            LaunchTimer(3,KillNode)
            
        

        

