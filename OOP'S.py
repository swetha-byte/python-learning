
### writing a class for rect:

# class rectangle:
#     def __init__(self,l,b):
#         self.len = l
#         self.bre = b

#     def area(self):
#         return self.len * self.bre

#     def vol(self):
#         return 2*(self.len + self.bre)    
    
# r = rectangle(12,10)
# print(r.area())
# r1 = rectangle(13,10)
# print(r1.vol())        



### writing a class for cuboid :

class cuboid:
    
    def __init__(self,l,b,h):
        self.len = l
        self.bre = b
        self.hei = h

    def lidarea(self):
        return self.len*self.bre

    def vol(self):
        return  self.len*self.bre*self.hei 

    def totalarea(self):
        return   2*(self.len*self.bre + self.bre*self.hei + self.hei*self.len)
    
c = cuboid(10,9,8)
print(c.vol()) 
print(c.lidarea())
print(c.totalarea())   