'''2. Rectangle nomli klass yarating. Klass namunasi height va width atributlarini qabul qiladi. Rectangle klassida quyidagi metodlarni yarating:
- get_height – Rectangle ob’ektining bo’yini qaytaradi
- set_height – Rectangle ob’ektining bo’yini o’zgartiradi
- get_width – Rectangle ob’ektining enini qaytaradi
- set_width – Rectangle ob’ektining enini o’zgartiradi
- get_area – Rectangle ob’ektining yuzasini hisoblab qaytaradi
- get_perimeter – Rectangle ob’ektining perimetrini qaytaradi
- get_info – Rectangle ob’ektining bo’yi, enini, yuza va perimetr to’g’risida to’liq ma’lumot beradi'''

class Rectangular:
    def __init__(self, height, width):
        self.height = height
        self.width = width


    def get_height(self):
        return f"Height: {self.height}"
    
    def set_height(self, new_height):
        self.height = new_height
        return f"New height is {self.height}"
    
    def get_width(self):
        return f"Width is {self.width}"
    
    def set_width(self, new_width):
        self.width = new_width
        return f"New width is {self.width}"
    
    def get_area(self):
        return f"Area of Rectangular is {self.height * self.width}"
    
    def get_perimetr(self):
        return f"Peremetr is {2 * (self.height + self.width)}"

    def get_info(self):
        return f"Height -> {self.height}, widht -> {self.width}, Area-> {self.get_area()}, Perimetr-> {self.get_perimetr()}"
    
    



