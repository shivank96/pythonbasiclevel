class Memory:
    def __init__(self,internal,secondary,ram):
        self.internal=internal
        self.secondary=secondary
        self.ram=ram
    def getMemoryInfo(self):
        print("internal storage is:{}, secondary storage is:{} and ram is:{}".format(self.internal,self.secondary,self.ram))
class Mobile:
    def __init__(self,model,brand,price,memory):
        self.model=model
        self.brand=brand
        self.price=price
        self.memory=memory
        # Mobile.getMobileFeatures(self)
    def getMobileFeatures(self):
        print("{}{} costs rs{}".format(self.brand,self.model,self.price))
        mem.getMemoryInfo()
mem = Memory('32gb','256gb','4gb')
mob= Mobile('7','samsung',12000,mem)
mob.getMobileFeatures()

