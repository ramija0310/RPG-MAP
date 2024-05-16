########################################################################
# Title : RPG - MAP
# Class : Computer Science 30
# Assighnment : Movement in the map
# Coder : Ramija Iffat
# Version : 1
########################################################################
""" In this game the player will just move around and explore any room 
    as he/she wants.
"""
########################################################################
# Functions-------------------------------------------------------------
house ={ "starting_room":{
                          "description" : "You are in the starting room.",
                          "items around the room" : ["dusty vase",
                                                    "broken mirror"],
                          "action" : "may start your game"
                         },
        "bedroom": {
                    "description" : "You have entered in a bedroom",
                    "items around the room" : [ "cranky bed",
                                                    "old table",
                                                    "broken closet",
                                                    "broken wardrobe"],
                    "action" : "may look around or rest"
                    },
        "washroom":{
                    "description" : " Woo! Filthy broken washroom. Be careful from" 
                                    + " the spider bites!",
                    "items around the room": [ "dusty toilet",
                                               "turnished sink"],
                    "action" : "may look around or rest."
                    },
        "living_room":{
                        "description" : "You have entered the living room. "
                                        + "Move quick! You can't be seen from "
                                        + "outside! Enemies might know where "
                                        + "you are here",
                        "items around the room" : [ "dusty couch",
                                                    "broken coffee table",
                                                    "dead fire place"],
                        "action" : "must run away or move to another location"
                       },
        "spooky_hallway":{
                            "description" : "You have entered the SPOOKY HALLWAY!" 
                                            + " DEFEAT GHOSTS!",
                            "items around the room" : [ "spider webbed curtains",
                                                        "dusty vase",
                                                        "swinging chandelier"],
                            "action" : "Defeat enemies!"
                          },
        "dinning_room":{
                        "description" : "Not much around",
                        "items around the room" : ["dusty dinning table",
                                                   "spider webbed chairs"],
                        "action" : "May rest or move to another location"
                        },
        "storage":{
                    "description" : " location for weapons",
                    "items around the room" : ["dirty cardboard box",
                                               "broken picture frame",
                                               "toys"],
                    "action" : "May pick weapon or move to another location"
                   },
        "study_room":{
                        "description" : " Some books and resources around",
                        "items around the room" : [ "fragile chair",
                                                    "dusty table",
                                                    "webbed and dusty book shelves"
                                                    "blinking lightlamp"],
                        "action" : "look for the storage key"
                      },
        "secret_room":{
                        "description" : " Mystery room ",
                        "items around the room" : "",
                        "action" : "open the storage room and see if you can find "
                                    + "something there. Be aware of enemies"    
                       }

        }
map1 = [
        ["living_room", "study_room", "bedroom", "washroom"],
        ["starting_room", "spooky_hallway", "spooky_hallway", "bedroom"],
        ["living_room", "dinning_room", "secret_room", "storage"]
       ]

# Imports and Global Variables----------------------------------------
import map
#import inventory
action = ["move", "explore"]

directions = ["north", "south", "west", "east"]

x = 1
y = 0

player_position = {
    "row":x, 
    "column":y
}
main = True


# Functions-------------------------------------------------------------
def main1():
    print("Welcome to the treasure hunt. You are in starting room. Good luck in your treasure hunt!")
    print("What do you want to do\n")
    global main, action
    while main:
        for actions in action:
            print(f" - {actions}")
        action_choice = input("\n Choose option: ")
        if action_choice.lower() == "explore":
            print("Have fun exploring around!")
        elif action_choice.lower() == "move":
            movement()


def movement():
    global main
    for direction in directions:
        print(f" - {direction}")
    print("It you want to quit. Type 'quit'. ")
    move1 = True
    while move1:
        ask_direction = input("\n Choose Direction: \n")
        if ask_direction.lower() == "north":
            if player_position["row"] == 0:
                print("No more North!")
            else:
                player_position["row"] -= 1
                move1 = False
        elif ask_direction.lower() == "south":
            if player_position["row"] == 2:
                print("No more South!")
            else:
                player_position["row"] += 1
                move1 = False
        elif ask_direction.lower() == "east":
            if player_position["column"] == 3:
                print("No more East!")
            else:
                player_position["column"] += 1
                move1 = False
        elif ask_direction.lower() == "west":
            if player_position["column"] == 0:
                print("No more West!")
            else:
                player_position["column"] -= 1
                move1 = False
        elif ask_direction.lower() == "quit":
            print("You are leaving.")
            move1 = False
            main = False
            
        else:
            print("Please Choose from the option")
    if main:
        room = house[map1[player_position["row"]][player_position["column"]]]["description"]
        print(room)
        item = house[map1[player_position["row"]][player_position["column"]]]["items around the room"]
        print(f"Items in the room {item}\n")
    #movement()

#Main-------------------------------------------------------------------
main1()    
map.export_map()
#inventory.export_inventory()