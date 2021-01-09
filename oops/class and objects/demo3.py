class Tv:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def features(self):
        print(self.brand+self.model," has following features:")
        print("This is a smart tv")
        print("can access internet")
        print("Has spport of latest Android version")
class SmartTv(Tv):
    def __init__(self, model, brand,screensize,price,resolution):
        super().__init__(model,brand)
        self.screensize=screensize
        self.price=price
        self.resolution=resolution
        SmartTv.features(self)
        SmartTv.newfeatures(self)
    def newfeatures(self):
        print(self.brand + self.model," has a ",self.screensize,"inch screensize with a ",self.resolution," resolution which costs",self.price)

Tv_model_name = input("Enter Tv model name")
Tv_brand_name = input("Enter Tv brand name")
screen_size=input("Enter screensize")
resolution=input("Enter resolution")
price=input("Enter price")
t=SmartTv(Tv_model_name,Tv_brand_name,screen_size,resolution,price)
