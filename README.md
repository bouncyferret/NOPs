![NOPS Icon](icon.jpeg)
# Nightmare OPerators
## Make NOPstimal use of your time in Houdini!

. . . How long can **you** survive? . . .

# Installation:

Download NOPs on your computer. You can use `git clone https://github.com/bouncyferret/NOPs.git` if you're familiar with `git`.

### Option 1 (recommended):


For the best NOPs experience, use one of our startup scripts to launch a clean Houdini with only NOPs installed.

`Windows:` Double click `start_NOPs_WINDOWS.bat`
`Linux:` `cd` to your NOPs install and run `sh ./start_NOPs_LINUX.sh`.

### Option 2 (manual install and launch):

Copy `NOPS.json` to `$HOME/houdini20.0/packages`
Edit `NOPS.json` to point to your NOPs install. You must not point to the root of the install but to the `houdini` directory.

`"NOPS": "/path/to/NOPs/houdini/"`

Once you've edited the json, run Houdini like you usually would.

You can launch Houdini without NOPs by setting `"enable": "false"` in `NOPs.json`. That allows you to easily switch between a NOPs-less (_funless_) session and a NOPs-enhanced session.

# NOPs features

We'll let you explore what NOPs has to offer but know that NOPs has a main menu  -- top left of your UI next to `File`, `Edit`, and the like -- that lets you set the level of awesomeness you can experience.

### Notes

NOPs is an april's fool idea by _BouncyFerret_ and _WaffleBoyTom_.

Feel free to let us know how we can improve NOPs !

Thank you for reading this and using NOPs < 3