"""class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
man = Celsius()
man.temperature = 37 # set temperature

print(man.to_fahrenheit())"""

# Using getters and setters
class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)
    
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    # new update
    def get_temperature(self):
        return self.temperature
    
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature is below -273.15")
        self.temperature = value

