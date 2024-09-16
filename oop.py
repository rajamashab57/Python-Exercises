class car():
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self) :
        return f'a {self.color} car'
mycar = car("red",2300)

print(type(mycar))
# mycar
        