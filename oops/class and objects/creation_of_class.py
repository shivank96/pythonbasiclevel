class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.__b = b
    def area(self):
        return self.l*self.__b
c=Rectangle(10,15)
_c=Rectangle(10,20)
print(_c.area())
# print(_c._Rectangle__b)//name mangling or accessing private variable
print(dir(c))
print(c.l)
help(c.area)
print(c.area())