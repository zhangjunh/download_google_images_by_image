from spider import spiders
from merge import merges
from finalmerge import finalmerges
import os
from delrepetition import delrepetitions
from convert import converts
from rename import renames

allpath = os.getcwd()
database = os.path.join(allpath, "train")

retry = 1
while retry:
    try:
        retry = 0
        spiders(allpath)

    except:
        retry = 1
        print("START AGAIN")

merges(allpath)
print("Merged.")
finalmerges(allpath, database)
print("First finalmerged.")
delrepetitions(allpath)
print("Deleted.")
converts(allpath)
print("Converted.")
finalmerges(allpath, database)
print("Last finalmerged.")
renames(allpath)
print("All completed.")
