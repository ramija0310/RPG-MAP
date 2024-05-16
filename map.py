# Imports and Global Variables------------------------------------------
from tabulate import tabulate
max_row = 2
max_column = 3
#game's map made with an array
tile = [
        ["living room", "study room", "bedroom", "washroom"],
        ["starting room", "spooky hallway", "spooky hallway", "bedroom"],
        ["living room", "dinning room", "secret room", "storage"]
       ]

#maps external filename
mapfile = "map.txt"


# Functions-------------------------------------------------------------
def export_map():
    try:
        with open(mapfile, 'w') as file:
            file.write(tabulate(tile, tablefmt = 'fancy_grid'))
    except:
        print("File failed to write")
    else:
        print("")
    finally:
        print("")

def read_map():
    try:
        with open(mapfile,'r') as file:
            print(file.read())
    except:
        print("Unable to show map")
    else:
        print("")
    finally:
        ("Hopefully it helps.")


#Main-------------------------------------------------------------------
export_map()
read_map()