# Copyright 2021 by DADON#4076 
# All rights reserved.
# This file is part of the Arcaea hacking efforts
# and is released under GPLv3 Please see the LICENSE
# https://www.gnu.org/licenses/gpl-3.0.en.html



import json
import os
import glob


with open("arc.json", "r") as f:
    a_dict = json.load(f)
    groups = a_dict["Groups"]
    f.close()
JSON = open("arc.new.json", "w+")
arc = open("arc.pack", "ab")

shiftedOffset = 0
currLength = 0

for group in groups:
    print("---", group["Name"], "---")
    print("Current Offset : ", currOffset)
    group["Offset"] = group["Offset"] + shiftedOffset
    currLength = 0
    for entry in group["OrderedEntries"]:
            filesize = os.path.getsize("archive/" + entry["OriginalFilename"])
      #      print(entry["OriginalFilename"])
      #      print(entry["Offset"])
      #      print(entry["Length"])
            entry["Offset"] = shiftedOffset + entry["Offset"]
            if os.path.getsize("archive/" + entry["OriginalFilename"]) != entry["Length"]:
                filename = "archive/" + entry["OriginalFilename"]
                with open(filename, "rb") as file:
                    arc.seek(entry["Offset"])
                    arc.write(file.read())
                currOffset += filesize
                currLength += filesize
            filename = "archive/" + entry["OriginalFilename"]
            with open(filename, "rb") as file:
                arc.write(file.read())
            entry["Length"] = filesize
    group["Length"] = currLength
    print("Final Offset : ", currOffset)

JSON.write(json.dumps(a_dict, indent=2,))

JSON.close()
arc.close()

                
