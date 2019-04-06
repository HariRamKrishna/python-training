class Dress:
  def __init__(self, name, material,brand,price ):
    self.name = name
    self.material = material
    self.brand= brand
    self.price=price

  def wash_self(self):
    print("Your "+self.name+" will be washed")
  def iron_self(self):
    print("your "+ self.name+" will be ironed")
  def cut_self(self):
    print("your "+self.name+"will be cut")

p1 = Dress("Sweater", "wool", "Nepali", '4000')
p2=Dress("Paint","Jeans" , "Indian","1500")
p3=Dress("shirt","Weaved","Nepali",'1000')
p3.iron_self()
p2.wash_self()



