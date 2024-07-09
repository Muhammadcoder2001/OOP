from datetime import datetime
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time(self):
        if self.second > 59:
            self.minute + 1
            self.second = self.second % 60
        if self.minute > 59:
            self.hour + 1
            self.minute = self.minute % 60
        if self.hour > 23:
            self.hour = self.hour % 24
            return f"{self.hour :02d}:{self.minute :02d}:{self.second :02d}"
        
    def get_hour(self):
        if self.hour > 23:
            self.hour = self.hour % 24
            return f"Hour: {self.hour :02d}"
        return f"Hour: {self.hour :02d}"
            
    
    def get_minute(self)->int:
        if self.minute > 59:
            self.minute = self.minute % 60
            return f"Minute: {self.minute :02d}"
        
        return f"Minute: {self.minute :02d}"
        
    
    def get_second(self):
        if self.second > 59:
            self.second = self.second % 60
            return f"Second: {self.second :02d}"
    
    def set_hour(self, new_hour):
        self.hour = new_hour
        self.hour = self.hour % 24
        return f"Changed hour: {self.hour :02d}"

    def set_minute(self, new_minute):
        self.minute = new_minute
        if self.minute > 59:
            self.hour = self.hour + 1
            self.minute = self.minute % 60
            return f"Changed minute: {self.minute :02d}"
        
        return f"Changed minute: {self.minute :02d}"
        

    def set_second(self, new_second):
        self.second = new_second
        if self.second > 59:
            self.second = self.second % 60
            self.minute = self.minute + 1
            return f"Changed second: {self.second :02d}"

        return f"Changed: {self.second}"
    
    def set_time(self, new_hour, new_minute, new_second):
        self.hour = new_hour
        self.minute = new_minute
        self.second = new_second
        if self.second > 59:
            self.second = self.second % 60
            self.minute += 1
        if self.minute > 59:
            self.minute = self.minute % 60
            self.hour += 1
        if self.hour > 23:
            self.hour = self.hour % 24
            return f"Hour: {self.hour} Minute: {self.minute} Second: {self.second}"
        
        return f"Hour: {self.hour} Minute: {self.minute} Second: {self.second}"
    
    def toString(self):
        return f"{self.hour :02d}:{self.minute :02d}:{self.second :02d}"

    def previous_second(self):
        # self.second -= 1
        if self.second == 0:
            self.second = 59 
            self.minute -= 1
        if self.minute == 0:
            self.minute = 59
            self.hour -= 1
        if self.hour == 0:
            self.hour = 23
            return f"{self.hour :02d}:{self.minute :02d}:{self.second :02d}"

        return f"{self.hour :02d}:{self.minute :02d}:{self.second - 1 :02d}"
        
    def next_second(self):
        #  self.second += 1
        if self.second > 59:
            self.second %= 60 
            self.minute += 1
        if self.minute > 59:
            self.minute %= 60
            self.hour += 1
        if self.hour > 23:
            self.hour %= 24
            return f"{self.hour :02d}:{self.minute :02d}:{self.second :02d}"

        return f"{self.hour :02d}:{self.minute :02d}:{self.second + 1 :02d}"


duration = Time(24, 74, 84)
print(duration.get_hour())
print(duration.get_minute())
print(duration.get_second())
print(duration.set_hour(27))
print(duration.set_minute(60))
print(duration.set_second(102))
print(duration.set_time(23, 30, 20))
print(duration.toString())
print(duration.next_second())
print(duration.previous_second())



