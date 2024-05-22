

class object():
  def __init__(self, name, description, location):
    self.name = name
    self.description = description
    self.location = location
    
class weapons(object):
  def __init__(self, name, description, location, damage):
    self.description = description
    self.location = location 
    self.damage = damage

baseball_bat = weapons("Baseball bat", "Helpful for attacking enemies", [2, 3], -30)
pickaxe = weapons("Pickaxe", "Helpful for attacking enemies", [1,1], -40)
torch = object("Torch", "lights are needed in this dark place.", [0,1])
Chest = object("Chest", "You have found th echets look inside!", [2,3])

location = [
            ["living room", "study room", "bedroom", "washroom"],
            ["starting room", "spooky hallway", "spooky hallway", "bedroom"],
            ["living room", "dinning room", "secret room", "storage"]
           ]

