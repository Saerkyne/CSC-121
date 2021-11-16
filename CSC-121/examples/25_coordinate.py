

# Author: Michael Souther
# Date: 10/28/2019
# Purpose: To demo classes
class Coordinate(object):
   def __init__(self, initial_x, initial_y):
      self.x=initial_x
      self.y=initial_y

   def __str__(self):
      return "<" + str(self.x) + "," + str(self.y) + ">"

   def distance(self, other_coordinate):
      """ Calc the distance between two coordinate """
      x_diff_squared=((self.x - other_coordinate.x)**2)
      y_diff_squared=((self.y - other_coordinate.y)**2)
      distance=(x_diff_squared + y_diff_squared)**0.5
      return distance
   def set_x_value(self,new_x):
      self.x = new_x
   def set_y_value(self,new_y):
      self.y = new_y
   def get_x_value(self):
      return self.x
   def get_y_value(self):
      return self.y

coord1 = Coordinate(3,4)
coord2 = Coordinate(1,2)
print(coord1)
print(coord2)
print(str(coord1.distance(coord2)))
coord1.set_x_value(4)
coord1.set_y_value(6)
print(coord1)
print(coord2.get_x_value())
print(coord2.get_y_value())

