from __future__ import print_function
import hou
import nodegraphprefs as prefs
import nops_utils as nut
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
            title+= "Dive into Sops, quick !"
        elif label == "motion fx":
            title += "You're in the forbidden context ... get out !"
        elif label == "geometry":
            title += "Work that Sops magic... if you can ?"
        elif label == "solaris":
            title += "Why would you leave Sops ? This context is scary !"
        elif label == "vex builder":
            title += "Writing code > whatever you're doing in this context..."
        elif label == "tasks":
            title += "The Best Context"
        elif label == "compositing":
            title += "Careful, this context is full of Cops !"
        elif label == "dynamics":
            title+= "You're not thinking of doing FLIP are you ??"
        elif label == "shaders":
            title += "You must be lost..."
        elif label == "outputs":
            title += "You're not exporting to another package, are you ?"
        else:
            title += "What kind of context are you in ??!"
        
    except Exception as e:
        
        title = f"My Script failed : ( because of {e}"

    return title

