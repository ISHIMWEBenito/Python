class Polygon:
    def _init_(self, no_of_sides):
        self.n = no_of_sides
        self.sides =  []
        for i in range(no_of_sides):
            self.sides.append(0)
    def input_sides(self):
        for i in range(self.n):
            self.sides[i] = float(input("Enter side"+str(i+1)+" : "))
            
#inheriting Triangle from Polygon Class
class Triangle(Polygon):
    def _init_(self):
        Polygon._init_(self, 3)
        
    def find_area(self):
        a, b, c = self.sides
        #calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is', area)
        
        t = Triangle()
        t.input_sides()
        t.find_area()