import random
from typing import List, Dict, Any, Match
import re
import os
import json

# if NOPS is not in env -> assume that it's executed from NOPs root dir
nopsPath: str = os.getenv("NOPS", ".")

# load config to check if random_fonts is enabled
with open(f"{nopsPath}/nops_prefs.json") as file:
    nopsConfig: Dict[str, Any] = json.loads(file.read())

if "randomize_fonts" in nopsConfig:
    nopsRandomizeFonts: bool = nopsConfig["randomize_fonts"]
else:
    nopsRandomizeFonts = False

# load font resources template
templatePath: str = nopsPath + "/config/resources_template"
with open(templatePath, "r") as file:
    templateFile: str = file.read()

if nopsRandomizeFonts:
    print("Ranomizing Fonts")

    fontsCsvPath: str = nopsPath + "/csvs/fonts.csv"
    with open(fontsCsvPath, "r") as file:
        fontList: List[str] = file.read().splitlines()

    newConfig: List[str] = []
    for config in templateFile.splitlines():
        match = re.search(r"Proportional|Fixed|Black", config)
        if match:
            newFont: str = random.choice(fontList)
            config = config.replace(match.group(), newFont)

        newConfig.append(config + "\n")

    with open("config/resources", "w") as file:
        file.writelines(newConfig)
else:
    print('Restoring "Default" Fonts')

    with open("config/resources", "w") as file:
        file.writelines(templateFile)
