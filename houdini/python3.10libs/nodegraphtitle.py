from __future__ import print_function
import hou
import nodegraphprefs as prefs
import nops_utils as nut
import nops_rand as nr 
from typing import List

def networkEditorTitleLeft(editor):
    try:
        difficulties: List[str] = ["Ouch !","Very Ouch !", "Nightmare !", "Traumatize me !"]
        index: int = nut.LoadDifficultyIndex()
        
        title = f"Pain level = {difficulties[index]}\r Node Count = {len([n for n in hou.node('/').allSubChildren()])}"
        pwd = editor.pwd()
        playerparm = pwd.parm('isplayer')
        if playerparm is not None and playerparm.evalAsInt() != 0:
            title += 'Network in Playback Mode\n'
        if prefs.showPerfStats(editor):
            profile = hou.perfMon.activeProfile()
            if profile is not None:
                profiletitle = profile.title()
                if not profiletitle:
                    profiletitle = 'Profile ' + str(profile.id())
                title += profiletitle + ': ' + prefs.perfStatName(editor)

    except:
        title = ''

    return title

def networkEditorTitleRight(editor):
    
    
    try:
        title = ''
        pwd = editor.pwd()
        label: str = pwd.childTypeCategory().label().lower()
        if label == "objects":

            title_tuple: tuple[str] = ("Dive into Sops, quick !",
                                       "Don't transform stuff in here !",
                                       "I object to you being here")
            
            title+= title_tuple[nr.ChooseFromStringArray(title_tuple)]
        
        elif label == "motion fx":
            
            title_tuple: tuple[str] = ("You're in the forbidden context ... get out!",
                                       "Good luck",
                                       "Here for the jiggle?")
            
            title += title_tuple[nr.ChooseFromStringArray(title_tuple)]
        
        elif label == "geometry":
            
            title_tuple: tuple[str] = ("Work that Sops magic ... if you can !",
                                       "The context we all know and love",
                                       "Sops ? How original ...")
            
            title += title_tuple[nr.ChooseFromStringArray(title_tuple)]        
        
        elif label == "solaris":
            
            title_tuple: tuple[str] = ("Why would you leave Sops ? This context is scary !",
                                      "LIVERPEACE or whatever",
                                      "USDa-mazing context if you want my opinion. So many layers to this joke")
            
            title += title_tuple[nr.ChooseFromStringArray(title_tuple)]        
        
        elif label == "vex builder":
            
           title_tuple: tuple[str] = ("Writing code > whatever you're doing in this context ...",
                                      "Here for the noise I presume",
                                      "VOPspaghetti")
            
           title += title_tuple[nr.ChooseFromStringArray(title_tuple)]        
        
        elif label == "tasks":

            title_tuple: tuple[str] = ("TOPs is love TOPs is life",
                                      "The Best Context",
                                      "You're awesome <3")
            
            title += title_tuple[nr.ChooseFromStringArray(title_tuple)]        
        
        elif label == "compositing":

            title_tuple: tuple[str] = ("Careful, this context is full of Cops !",
                                      "Needs more glow",
                                      "How DO you bake Aces in ??")
            
            
            title += title_tuple[nr.ChooseFromStringArray(title_tuple)]
        
        elif label == "dynamics":
            
            title_tuple: tuple[str] = ("You're not thinking of doing FLIP are you ??",
                                      "Solving is hard huh",
                                      "Someone thinks they're a physicist...")
            
            title += title_tuple[nr.ChooseFromStringArray(title_tuple)]        
        
        elif label == "shaders":

            title_tuple: tuple[str] = ("You must be lost ...",
                                      "How did you even get here ?",
                                      "Maybe you know something I don't ?")
            
            title += title_tuple[nr.ChooseFromStringArray(title_tuple)]        
        
        elif label == "outputs":

            title_tuple: tuple[str] = ("You're not exporting to another package, are you?",
                                      "Who ROPed you into this ?",
                                      "Please tell me you're using this with TOPs")          
            
            title += title_tuple[nr.ChooseFromStringArray(title_tuple)]
        
        
        else:
            
            title_tuple: tuple[str] = ("What kind of context are you in ??!",
                                      "APEXcellent",
                                      "You clearly have no fear")
            
            
            title += title_tuple[nr.ChooseFromStringArray(title_tuple)]        
    
    
    except Exception as e:
        
        title = f"My Script failed : ( because of {e}"

    return title

