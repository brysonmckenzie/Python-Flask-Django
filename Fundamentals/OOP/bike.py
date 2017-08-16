class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 
        



    def  Displayinfo(self):
            print "Price: $",self.price, "Max Speed: ", self.max_speed," - Total Miles: ", self.miles
    
    def Ride(self):
        self.miles += 10
        print "Riding:", "Total Miles: ",self.miles

    def reverse(self):
        self.miles = self.miles - 5
        print "Reversing:", "Total Miles: ", self.miles


bike1 = Bike(200,"25 mph")
bike2 = Bike(300,"35 mph")
bike3 = Bike(250,"10 mph")  

bike1.Displayinfo()
bike2.Ride()
bike2.reverse()




        







        