from enum import StrEnum
from typing import List

class Context(StrEnum):
    OBJ = "objects"
    CHOPS = "motion fx"
    SOPS = "geometry"
    LOPS = "solaris"
    VOPS = "vex builder"
    TOPS = "tasks"
    COPS2 = "compositing"
    COPS = "copernicus"
    DOPS = "dynamics"
    SHOPS = "shaders"
    ROPS = "outputs"
    APEX = "apex"


theContextPrompts: dict = {
    
    Context.OBJ.value    : ("Dive into Sops, quick !",
                            "Don't transform stuff in here !",
                            "I object to you being here"),
    
    Context.CHOPS.value  : ("You're in the forbidden context ... get out!",
                            "Good luck",
                            "Here for the jiggle?"),
    
    Context.SOPS.value   : ("Work that Sops magic ... if you can !",
                            "The context we all know and love",
                            "Sops ? How original ..."),
    Context.LOPS.value   : ("Why would you leave Sops ? This context is scary !",
                            "LIVERPEACE or whatever",
                            "USDa-mazing context if you want my opinion. So many layers to this joke"),
    
    Context.VOPS.value   : ("Writing code > whatever you're doing in this context ...",
                            "Here for the noise I presume",
                            "VOPspaghetti"),
    
    Context.TOPS.value   : ("TOPs is love TOPs is life",
                            "The Best Context",
                            "You're awesome <3"),
    
    Context.COPS2.value  : ("Careful, this context is full of Cops !",
                            "Needs more glow",
                            "How DO you bake Aces in ??"),
    
    Context.COPS.value   : ("ENHANCE !", 
                            "The New SOPs I guess ?", 
                            "No timeshift here, don't ask..."),
    
    Context.DOPS.value   : ("You're not thinking of doing FLIP are you ??",
                            "Solving is hard huh",
                            "Someone thinks they're a physicist..."),
    
    Context.SHOPS.value  : ("You must be lost ...",
                            "How did you even get here ?",
                            "Maybe you know something I don't ?"),
    
    Context.ROPS.value   : ("You're not exporting to another package, are you?",
                            "Who ROPed you into this ?",
                            "Please tell me you're using this with TOPs"),          
    
    Context.APEX.value   : ("What kind of context are you in ??!",
                            "APEXcellent",
                            "You clearly have no fear")
}

theDifficulties: List[str] = [
    "Ouch !",
    "Very Ouch !", 
    "Nightmare !", 
    "Traumatize me !"
]

