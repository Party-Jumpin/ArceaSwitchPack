# Copyright 2021 by Party Jumpin
# All rights reserved.
# This file is part of the Arcaea hacking efforts
# and is released under GPLv3 Please see the LICENSE
# https://www.gnu.org/licenses/gpl-3.0.en.html



import json
import os
with open("arc.new.json", "r") as f:
    a_dict = json.load(f)

archive = open("arc_result.pack", "rb")

groups = a_dict["Groups"]

for group in groups:
    #print("---", group["Name"], "---")
    for entry in group["OrderedEntries"]:
            #print(entry["OriginalFilename"])
            #print(entry["Offset"])
            #print(entry["Length"])

            paths ="archive/" + os.path.dirname(entry["OriginalFilename"])
            try:
                os.makedirs(paths)
            except:
                pass
            f2 = open("archive/" + entry["OriginalFilename"], "ab")
            archive.seek(entry["Offset"])
            data = archive.read(entry["Length"])
            f2.write(data)
            #f2 = (open("filenames.txt", "a"))
            #f2.write(entry["OriginalFilename"])
            #f2.write("\n")

archive.close()
f2.close()
