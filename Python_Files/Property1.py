class Celsius:
    def __int__(self, temperature = 0):
        self.temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    def get_temperature(self):
        print("Getting value")
        return self._temperature
    
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature is below -273.15")
        print("Setting value", value)
        
        self._temperature = value
        
    temperature = property(get_temperature,set_temperature)
    
c = Celsius(25)
        