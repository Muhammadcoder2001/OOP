'''
Date
-day:int
-month:int
-year:int

+Date(day:int,month:int,year:int)
+getDay():int
+getMonth():int
+getYear():int
+setDay(day:int):void
+setMonth(month:int):void
+setYear(year:int):void
+setDate(day:int,month:int,year:int):void
+toString():String

day = [1, 31]
month = [1, 12]
year = [1900, 9999]
No input validation needed.

"dd/mm/yyyy" with leading zero

5. Date nomli klass yarating. Unda quyidagi rasmda ko’rsatilgan atribut va metodlarni yarating.

'''

class Data:
    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year


    def date(self):
        return f"Day: {self.day} Month:{self.month} Year: {self.year}"
    
    def get_day(self):
        return f"Day: {self.day}"
        

    def get_month(self):
        return f"Month: {self.day}"
    
    def get_year(self):
        return f"Year: {self.year}"

    def set_day(self, new_day:int):
        self.day = new_day
        return f"Changed day: {self.day}"
    
    def set_month(self, new_month:int):
        self.month = new_month
        return f"Changed month: {self.month}"
    
    def set_year(self, new_year:int):
        self.year = new_year
        return f"Changed year: {self.year}"
    
    def set_date(self, new_day:int, new_month:int, new_year:int):
        self.day = new_day
        self.month = new_month
        self.year = new_year
        return f"Changed date: {self.day :02d}/{self.month :02d}/{self.year}"

    
    def toString(self):
        return f"{self.day :02d}/{self.month :02d}/{self.year}"
        
information = Data(9, 9, 2024)
print(information.get_day())
print(information.get_month())
print(information.get_year())
print(information.date())
print(information.set_day(8))
print(information.set_day(8))
print(information.set_day(8))
print(information.toString())
print(information.set_date(8, 8, 2024))





        


