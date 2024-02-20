import os
import hou
import json
from PySide2 import QtWidgets


class NopsPreferences(QtWidgets.QDialog):


    def __init__(self,parent):

        super(NopsPreferences,self).__init__(parent)
        self.Build()

    
    def SetDifficulty(self):

        nops_path: str = hou.getenv("NOPS")
        prefs_path: str = os.path.join(nops_path,"nops_prefs.json")
        
        with open(prefs_path,"w") as file:
            
            #prefs_data: dict = json.load(file)    
            
            prefs_data = dict()
            
            prefs_data["difficulty"]: int = self.menu.currentIndex() 
            
            json.dump(prefs_data,file)
        
        self.Close()
        

    def Close(self):

        self.close()

    def Build(self):

        self.setWindowTitle("NOPs Pain Level Dialog")

        main_layout: QtWidgets.QVBoxLayout  = QtWidgets.QVBoxLayout()

        chooser_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()

        pref_label: QtWidgets.QLabel = QtWidgets.QLabel("Choose your level of pain")

        self.menu: hou.qt.ComboBox = hou.qt.ComboBox()
        self.menu.addItem("Ouch !")
        self.menu.addItem("Very Ouch !")
        self.menu.addItem("Nightmare !")
        self.menu.addItem("Traumatize Me !")        
        
        chooser_layout.addWidget(pref_label)
        chooser_layout.addWidget(self.menu)

        main_layout.addLayout(chooser_layout)

        go_button: QtWidgets.QPushButton = QtWidgets.QPushButton("Set Difficulty")
        go_button.clicked.connect(self.SetDifficulty)
        
        leave_button: QtWidgets.QPushButton = QtWidgets.QPushButton("Cancel")
        leave_button.clicked.connect(self.Close)

        button_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(go_button)
        button_layout.addWidget(leave_button)

        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
         
