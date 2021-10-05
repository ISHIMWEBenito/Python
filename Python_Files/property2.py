class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature
        
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    @property
    def temperature(self):
        return self.temperature
    
    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature is below -273.15.")
        self._temperature = value
        
c = Celsius(25)
print(c.to_fahrenheit()) 