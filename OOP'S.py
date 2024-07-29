
### writing a class for rect:            ( 1 )

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



# ### writing a class for cuboid :        ( 2 )

# class cuboid:
    
#     def __init__(self,l,b,h):
#         self.len = l
#         self.bre = b
#         self.hei = h

#     def lidarea(self):
#         return self.len*self.bre

#     def vol(self):
#         return  self.len*self.bre*self.hei 

#     def totalarea(self):
#         return   2*(self.len*self.bre + self.bre*self.hei + self.hei*self.len)
    
# c = cuboid(10,9,8)
# print(c.vol()) 
# print(c.lidarea())
# print(c.totalarea())   



### WAYS OF CREATING INSTANCE VARIABLES:

# class test:                               (  3  )
#     def __init__(self):
#         self.a = 10

# t1 = test()
# print(dir(t1))


# class test:                               #(  4  )

#     def __init__(self):
#         self.a =10

#         def fun(self):
#             self.b = 20
# t1 = test
# t1.c =30            
# t1.fun()
# print(dir(t1))




## STATIC / CLASS VARIABLE & METHOD:        (  5  )

# class rectangle:
#     count = 0
    
#     def __init__(self,l,b):
#         self.len = l
#         self.bre = b
#         rectangle.count +=1

#     def perimeter(self):
#         return 2*(self.len + self.bre) 
#     def area(self):
#         return self.len * self.bre 
    
#     @classmethod
#     def classcount(cls):
#         print(cls.count)

    
# r1 = rectangle(20,10)
# print(r1.perimeter())   
# print(r1.area()) 
# print(rectangle.count)




### STATIC METHOD:                        (  6  )
 
# class rectangle:
    
#     def __init__(self,l,b):
#         self.len = l
#         self.bre = b

#     def perimeter(self):
#         return 2*(self.len + self.bre) 
#     def area(self):
#         return self.len * self.bre 

#     @staticmethod
#     def issquare(len , bre):
#         return len == bre
    
# r1 = rectangle(10,5)
# print(r1.issquare(11,10))  
# print(r1.perimeter())  



# ### ACCESSORS AND MUTATORS ( GET AND SET):      (  7  )

# class rectangle:

#     def __init__(self,l,b):
#         self.len = l
#         self.bre = b

#     def getlen(self):
#         return self.len 
#     def setlen(self,l):
#         self.len = l

#     def area(self):
#         return self.len * self.bre
#     def perimeter(self):
#         return 2*(self.len + self.bre)  
    
# r1 = rectangle(20,10)
# r2 = rectangle(10,15)
# print(r1.getlen())    
# print(r1.area())
# r2.setlen(20)
# print(r2.getlen()) 
# print(r2.area())



# ### INHERITANCE:                       (  8  )

# class rectangle:
#     def __init__(self,l,b):
#         self.len = l
#         self.bre = b
#     def area(self):
#         return self.len * self.bre 
#     def perimeter(self):
#         return 2 * (self.len + self.bre)    
    
# class cuboid(rectangle):
#     def __init__ (self,l,b,h):
#         self.hei = h
#         super().__init__(l,b)
#     def vol(self):
#         return self.len*self.bre*self.hei

# c = cuboid(30,20,10)
# print(c.vol())
# r = rectangle(20,10)
# print(r.area())           




###  POLYMORPHISM:                (  9  )

# def driver(car):
#     car.drive()

# class creata:
#     def drive (self):
#         print('creata is driving')
# class mercedes:
#     def drive(self):
#         print('mercedes is driving')

# c = mercedes()
# driver(c)                        



###  METHOD OVERLOADING:             (  10  )

# class arith:
#     def sum(self , a,b):
#         return a+b

# a = arith()
# print(a.sum(10,20))
# print(a.sum('hello','world'))


# class arith:                          #( error )
#     def sum(self,a,b):
#         return a+b
#     def sum(self,x,y,z):
#         return x+y+z
    
# a = arith()
# print(a.sum(1,2))    



# class arith:                        #( * )
#     def sum(self,a,b, c = None):
#         s = a+b
#         if c == None:
#             print (s)
#         else:
#             print(s+c)
# a = arith()
# (a.sum(10,20))                





### CLASS DICE :                          (   215  )

# from  random  import*
 
# class dice:
#     def __init__(self,sides):
#        self.sides = 12

#     def roll_dice(self):                                                  # def roll_dice(self,1,6):
#         return randint(1,self.sides)                                       # return random.randint
# d = dice(6)
# print(d.roll_dice())   
# print(d.roll_dice()) 



### CLASS FOR CIRCLE:                       (  216  )

# class circle:
#     def __init__(self,r):
#         self.rad = r

#     def area(self):
#         return ((22/7) *self.rad**2)
#     def perimeter(self):
#         return (2*(22/7) *self.rad) 

# c = circle(7)
# print(c.perimeter())
# print(c.area())    

    

### BOOK DETAILS:                             (   217  )

# class book:
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def show_details(self):
#         print('TITLE :',self.title)
#         print('AUTHOR :',self.author)
#         print('PRICE :',self.price)
    
# b = book('The Dany Summer Special','James',230)
# (b.show_details())    



### DETAILS OF AN EMPLOYEE:                      (   218  )

class employee:
    total_emp = 0
    emp_id = 101
    def __init__(self,name,designation,salary):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.emp_id = 'e'+ str(employee.emp_id)
        employee.total_emp += 1
        employee.emp_id += 1

    @classmethod
    def countemp(cls):
        print(cls.total_emp)
    def id(empid):
        print(empid.emp_id)  

    def show_details(self):
        print ('Name:',self.name)
        print('Empid:',self.emp_id)
        print('Designation:',self.designation)
        print('Salary:',self.salary)
        
emp1 = employee('swetha','accounts',200000)
(emp1.show_details()) 
print('')  
emp2 =  employee('arun','teamleader',500000)
(emp2.show_details()) 
print('Total :',employee.total_emp)
            








    
        




