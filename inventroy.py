
import random 

"""objects = ["Baseball bat", "pickaxe", "torch", "fire"]

objects = random.choice(objects)
print(object)"""

class object():
  def __init__(self, name, description, location):
    self.name = name
    self.description = description 
    self.location = location
    
class weapons(object):
    self.damage = damage


baseball_bat = object("Baseball bat", "Helpful for attacking enemies", [2, 4], -30)


class Baseball_bat(object):
  def __init__(self):
    self.name = ""
    self.damage = ""
    self.description = ""
    
class pickaxe(object):
  def __init__(self):
    self.name = "Pickaxe"
    self.damage = "-50"
    self.description = "Helpful for attacking enemies"
    
class torch(object):
  def __init__(self):
    self.name = "Torch"
    self.damage = None
    self.description = "Helpful for walking around with your lights in this dark place."

class fire_torch(object):
  def __init__(self):
    self.name = "fire torch"
    self.description = "Helpful for walking around with your fire torch in this dark place."
  