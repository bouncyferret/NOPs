import hou
from nops_constants import (
    theContextPrompts, 
    theDifficulties,
    theSymbolSize,
    theCoolNodes
)
import nops_rand as nr
import nops_utils as nut # yes, I'm childish, sue me... lol
import nops_needabreak as nap

# https://www.sidefx.com/docs/houdini/network/custom_info.html
# this has all the docs to customize node info window !

# we're adding context information which is
# the 'funny' stuff that shows up in your network editor.
# this category does not match the categories in the nodegraph title, fun!

label = category.lower()
label = nut.CategoryToContext(label)

title_tuple = theContextPrompts.get(
    label, 
    theContextPrompts["unknown"]
)

title = title_tuple[nr.ChooseFromStringArray(title_tuple)]

top.addLabeledText(f"You're in {category}: ", title)
top.addLabeledText("Banned Nodes: ", " - ".join(nut.GetBannedNodes()))


# can we tell if the node is marked for deletion ?
# answering my own question, yes we can !

if nut.IsBannedNode(node):
    addTag(
        "Marked For Deletion. Use Better Nodes...",
        color = theme.error,
        textColor = theme.teal,
        symbol = "flying-saucer",
        symbolSize = theSymbolSize
    )

# compliment user on node choice with a tag

if node.type().name() in theCoolNodes:
    addTag(
        "Great Node Choice!",
        color = theme.pink,
        textColor = theme.teal,
        symbol = "confetti",
        symbolSize = theSymbolSize
    )
    

# lets add the difficulty as a tag
index: int = nut.LoadDifficultyIndex()
addTag(
    theDifficulties[index]["label"],
    color = theme.fuchsia,
    textColor = theme.teal,
    # textSize = 32, seems like this is not supported ?
    symbol = theDifficulties[index]["icon"],
    symbolSize = theSymbolSize, #default is 16
    # symbolVariant 
)

# let people know NOPs is enabled with a tag

addTag(
    "You're using NOPs ! God knows why ...",
    color = theme.amber,
    textColor = theme.teal,
    symbol = "linux-logo",
    symbolSize = theSymbolSize, #default is 16
)


# add some marker of something ?
fun_amount = nr.GetRandomFloat()
other_fun_amount = nr.GetRandomFloat(654)
description = "Looks Like You're Struggling" if fun_amount < 0.5 else "Hell Yeah !" 
other_description = "Do Better" if fun_amount < other_fun_amount else "Good For You !"


item2 = addLabeledColumn("Fun Meter : ")
item2.addProgress(nr.GetRandomFloat())

# looks like drawing the arcs for the donuts are busted ...
# looks like arcColor does not work as a keyword...
addLabeledDonut("Fun Amount", fun_amount, 
                text=f"{(fun_amount/1.0)*100.0:.0f}%",
                description=description,
                start_angle = 0,
                end_angle = 360,
                arcColor = theme.teal,
                trackColor = theme.pink)

addLabeledDonut("Average Fun Amount", other_fun_amount, 
                text=f"{(other_fun_amount/1.0)*100.0:.0f}%",
                description=other_description,
                start_angle = 0,
                end_angle = 360,
                trackColor = theme.teal)


# random garbage here and there because we're having fun
grid = middle.addGrid()
grid.addSimpleTextTile("NOPS 2.0", "The Best Version Yet !")
grid.addSimpleTextTile("Made by", "Tom & Aslak")
grid.addSimpleTextTile("How did you manage to get anything done", "Without NOPs ?")

# we wholesome, we love you 
tile1 = addExpandingTile("Thank you <3", expanded=True)
tile1.addText("For Trying Out NOPs, We Really Appreciate It !")

def my_fun(shift=False):
    nap.AnnoyingCook(always=True)

# not sure how you would lay those next to each other
addButton("Enhance     ", my_fun)
addButton("Add Crunch  ", my_fun)
addButton("Scrunk It Up", my_fun)
addButton("Add Goodness", my_fun)

path = "$NOPS/media/catWizard.gif"
animated = True

if nr.RandomTrigger(0.75): # make the wizard somewhat rare
    random_index: int = nr.ChooseFromStringArray((0,0,0))                       
    path = f"$NOPS/media/logoNOPS{random_index}.jpeg"
    animated = False


top.addImage(hou.text.expandString(path), animated = animated)
