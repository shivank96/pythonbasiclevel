class car:
    def __init__(self,model,brand,color):
        self.model=model
        self.brand=brand
        self.color=color
    def start(self):
        print(self.brand+self.model," is starting")
    def move(self):
        print(self.brand+self.model," is moving")
    def stop(self):
        print("stopped the ",self.brand+self.model)
class BMWCar(car):
    def __init__(self,model,brand,color):
        super().__init__(model,brand,color)
        # We can do the following method calls which are called automatically when an object of this class is created
        # BMWCar.start(self)
        # BMWCar.move(self)
        # BMWCar.autopilot(self)
        # BMWCar.autogear(self)
        # BMWCar.stop(self)
    def autopilot(self):
        print("autopilot mode activated")
    def autogear(self):
        print("autogear is activated")
car_model_name=input("Enter car model name")
car_brand_name = input("Enter car brand name")
car_color=input("Enter color of car")
b = BMWCar(car_model_name,car_brand_name,car_color)
b.start()
b.move()
b.autopilot()
b.autogear()
b.stop()