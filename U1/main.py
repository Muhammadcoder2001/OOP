from math import pi

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


    def get_radius(self):
        return self.radius
        # print(f"{self.radius}")

    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius

    def get_color(self, color):
        self.color = color
        return self.color

    def set_color(self, new_color):
        self.color = new_color
        return self.color

    def get_area(self, radius):
        return pi * (radius ** 2)
    
    def get_circuference(self, radius):
        return 2 * pi * radius
 
    def get_info(self):
        return f"""Radiusi: {self.radius}  Rangi: {self.color}  yuzasi: {self.get_area(5)}""" 
        

object1 = Circle(3, "brown")
# print(object1.get_radius())
# print(object1.get_area(3))
# print(object1.get_circuference(4))
# print(object1.set_color("red"))
# print(object1.set_radius(6))
print(object1.get_info())

        