class vehicle:
    def move(self):
     print("the vehicle is moving on road")
    
class car(vehicle):
   def move(self):
    print("driving on the road")


class Bicycle(vehicle):
   def move(self):
     print("pedaling on the road")

     
#objects created
c1=car()
b1=Bicycle()


#calling
c1.move()
b1.move()