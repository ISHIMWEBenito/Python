class Polygon:
    def _init_(self, no_of_sides):
        self.n = no_of_sides
        self.sides = []
        for i in range(no_of_sides):
            self.sides.append(0)
            
    def input_sides(self):
        for i in range(self.n):
            self.side[i] = float(input("Enter side"+str(i+1)+" : "))
    
    def display_sides(self):
        for i in range(self.n):
            print("sides", i+1, "is", self.sides[i])
            
p1 = Polygon(3)
p1.input_sides()
p1.display_sides()