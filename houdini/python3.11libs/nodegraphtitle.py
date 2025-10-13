from __future__ import print_function
import hou
import nodegraphprefs as prefs
import nops_utils as nut
import nops_rand as nr 
from nops_constants import theContextPrompts, theDifficulties
from typing import List
from enum import StrEnum

def networkEditorTitleLeft(editor):
    try:
        index: int = nut.LoadDifficultyIndex()
        
        title = f"Pain level: {theDifficulties[index]}\r\nNode Count: {len([n for n in hou.node('/').allSubChildren()])}"
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

        title_tuple = theContextPrompts.get(
            label, 
            ("ASSERT ! ASSERT !", "OH GOD, WHAT HAPPENED !!", "WHERE ARE YOU ???")
        )
        title += title_tuple[nr.ChooseFromStringArray(title_tuple)]
    
    
    except Exception as e:
        
        title = f"My Script failed : ( because of {e}"

    return title

