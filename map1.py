class map():
  def __init__(self, name, description):
    self.name = name
    self.description = description
    
  def description(self):
    print(self.description) # description

starting_room = map("starting_room", "You are in the starting"),
bedroom = map("bedroom","You have entered in a bedroom"),
washroom = map("washroom", "Woo! Filthy broken washroom. Be careful" 
                          + "from the spider bites!"),
living_room = map("living_room", "You have entered the living room. "
                            + "Move quick! You can't be seen from "
                            + "outside! Enemies might know where "
                            + "you are here."
                         "spooky_hallway":{
                           "description" : "You have entered the SPOOKY HALLWAY!" 