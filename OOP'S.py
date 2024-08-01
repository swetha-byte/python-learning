
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



# ### DETAILS OF AN EMPLOYEE:                      (   218  )

# class employee:
#     total_emp = 0
#     emp_id = 101
#     def __init__(self,name,designation,salary):
#         self.name = name
#         self.salary = salary
#         self.designation = designation
#         self.emp_id = 'e'+ str(employee.emp_id)
#         employee.total_emp += 1
#         employee.emp_id += 1

#     @classmethod
#     def countemp(cls):
#         print(cls.total_emp)
#     def id(empid):
#         print(empid.emp_id)  

#     def show_details(self):
#         print ('Name:',self.name)
#         print('Empid:',self.emp_id)
#         print('Designation:',self.designation)
#         print('Salary:',self.salary)
        
# emp1 = employee('swetha','accounts',200000)
# (emp1.show_details()) 
# print('')  
# emp2 =  employee('arun','teamleader',500000)
# (emp2.show_details()) 
# print('Total :',employee.total_emp)
            




###  CLASS FOR CALCULATOR:                                (   220  )

# class calculator:
    
#     @staticmethod
#     def add(a,b):
#         return a+b
#     def sub(a,b):
#         return a-b
#     def mul(a,b):
#         return a*b
#     def div(a,b):
#         return a//b
# x=10
# y=30
# print(calculator.add(x,y))
# print(calculator.add(a=12,b=13))    
# print(calculator.sub(20,10))
# a=30
# b=15
# print(calculator.div(a,b))
# print(calculator.mul(a,b))




    
#  ###  CUSTOMER PHONE NUMBER:                       (   220  )       

# class customer:
#     def __init__(self,name,phoneno):
#         self.name1 = name
#         self.phno1 = phoneno

#     def get_name1(self):
#         return self.name1
#     def get_phno1(self):
#         return self.phno1
#     def set_phno1(self,ph):
#         self.phno1=ph
    
# c1 = customer('swetha',44234566547)
# print(c1.get_name1())
# print(c1.get_phno1())
# c1.set_phno1(91234522173)
# print('')
# print(c1.get_name1())
# print(c1.get_phno1())





### CURRENCY CONVERTER:                                      (   221  )

# class currency_converter:
#     def __init__(self,currency_name,rate):
#         self.currency = currency_name
#         self.rate = rate

#     def get_currency(self):
#         return self.currency
#     def set_currency(self,cur1):
#         self.currency = cur1

#     def get_rate(self):
#         return self.rate
#     def set_rate(self,rate1):
#         self.rate = rate1

#     def convert(self,amt):
#         amt1 = (self.rate * amt) 
#         return amt1
        

# cc = currency_converter('USD',70)
# print('currency :',cc.get_currency())
# print('rate :',cc.get_rate())
# print('convention :',cc.convert(100))
# print('')

# cc.set_currency('AUS')
# cc.set_rate(90)
# print(cc.get_currency())
# print(cc.get_rate())
# print(cc.convert(900))





# ###  BANK ACCOUNT:                                     (   222  )

# class MinimumBalanceError(Exception):
#     pass
# class account:

#     next_account_number = 1001

#     def __init__(self,name,balance):
#         if balance < 1000:
#             raise MinimumBalanceError('account cannot be created')
#         self.name = name
#         self.blnc = balance
#         self.account_number = account.next_account_number
#         account.next_account_number += 1 
        
#     def get_balance(self):
#         return self.blnc

#     def deposit(self,amount):
#         self.blnc = (self.blnc + amount)
#         return 'Deposit successfull:' + str(amount)

#     def withdraw(self,amount):
#         if (self.blnc-amount) >= 1000:
#             self.blnc=self.blnc-amount
#             return 'Withdrawl Successfull '+ str(amount)
#         else:
#             return 'Low Balance. Minimum Balnce should be 1000'
        
#     def show_details(self):
#         print('NAME :',self.name)
#         print('ACC_NUM :',self.account_number)
#         print('BALANCE :',self.blnc)

# # arun_ac = account('arun',900)

# num = account('swetha',1500)
# print(num.withdraw(300))
# (num.show_details())

# print(num.deposit(1000))
# print('Your Amount in account is,', num.get_balance())

# a = int(input("Enter amount to withdraw :"))
# print(num.withdraw(a))
# print('Your Amount in account is,', num.get_balance())
# print('')
# num1 = account('james', 1600) 
# (num1.show_details())
# print(num1.get_balance())
# print('withdraw amt is',num.withdraw(100))     
    



# ###  ACCOUNT BALANCE :   (   1  )

# class MinimumBalanceError(Exception):
#     pass

# class account:

#     next_account_num = 1001

#     def __init__(self,name,balance=1000):

#         if balance < 1000:
#            raise MinimumBalanceError('min 1000 is required to create an account' )
#         self.name = name
#         self.account=self.next_account_num
#         self.next_account_num += 1
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance = (self.balance + amount)
#         print('succefully deposited',amount)
#         return self.balance
    
    
#     def withdraw(self,amount):
#         if (self.balance - amount) >= 1000:
#             self.balance = self.balance - amount
#             return 'withdraw successful'+ str(amount)
#         else:
#             print('low balance ') 


#     def show_details(self):
#         print('NAME :', self.name )
#         print('ACC_NUM :',self.account)
#         print('ACC_BALANCE :',self.balance)
       
# num = account('JAMES',1500)
# # num.show_details()
# # print(num.deposit(1000))
# (num.withdraw(100))
# num.show_details()
# # print('')
# # num1 = account('SMITH',2000)
# # num1.show_details()
# # print('')
# # num2 = account('AJAY',3000)
# # num2.show_details()

        




### INHERITING SHAPES IN CLASSES:                         (   223  )

# import math
# class polygon:

#     def __init__(self,no_of_sides,*sides):
#         self.num_of_sides = no_of_sides
#         self.sides = sides

# class triangle(polygon):

#     def __init__(self,no_of_sides,*sides):
#         polygon.__init__(self,no_of_sides,*sides)

#     def area(self):
#         a ,b ,c = self.sides

#         s = (a+b+c)/2
#         area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#         return area

# t1 = triangle(3,10,15,9)
# print(t1.area())   




### ACEDEMIC COURSES:                            (   224  )

# class course:

#     def __init__(self,name,duration,*books):
#         self.course_name = name
#         self.course_duration = duration
#         self.books = [self.Book for x in range(str(books))]

#     class Book:
#         def __init__(self,title):
#             self.title = title
        
#         def __str__(self):
#            return str(self.Book)

# c1 = course('python','1hr','physics')    
# print(c1.Book())



# class course:

#     def __init__(self,name,dur,*books):

#         self.name = name
#         self.duration = dur
#         self.books = [self.Book(b) for b in books]

#     def show_details(self):

#         print('NAME :',self.name)
#         print('DURATION :',self.duration)
#         for b in self.books:
#             print(b)

#     class Book:

#         def __init__(self,title):
#             self.title = title
#         def __str__(self):
#             return self.title 

# c1 = course('python',10,'python learning','python learning course')
# c1.show_details()                   





###  DETAILS OF A COMPUTER:                           (   225  )

# class computer:

#     def __init__(self, name,make,os):

#         self.name = name
#         self.cpu = self.cpu(make)
#         self.os = self.os(os)

#         def show_details(self):
#             print(self.name)
#             print(self.cpu.get_make())
#             print(self.os.get_os())

#         def __str__(self):
        #     return 'NAME :'+self.name +'\nMake :' + self.cpu.get_make1() + '\nOS NAME :' +self.os.get_os1()


 
        
        # class CPU:

        #     def __init__(self,make):
        #         self.make1 = make
        #     def get_make1(self):
        #         return self.make1

        #     def __str__(self):
        #         return  self.make1  

        # class OS:
        #     def __init__(self,os):
        #         self.os1 = os
        #     def get_os1(self):
        #         return self.os1
            
        #     def __str__(self):
        #         return self.os1
            

        # def show_details(self):
        #     print(self.name)
        #     print(self.cpu.get_make())
        #     print(self.OS.get_os())    

            

# c1 = computer('hp','intel','linux')
  
# c1.show_details()                
                
           



###  PET DETAILS:                                  (   226  )


#   @ POLYMIRPHISM: (226)


# def my_pet(pet):
#     pet.info()
#     pet.make_sound()


# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print('My name is '+ self.name + ' My age is '+ str(self.age))

#     def make_sound(self):
#         print('meow meow')    

        


# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#           print('My name is '+ self.name + 'My age is '+str(self.age))  

#     def make_sound(self):
#         print('bow bow')


# # def my_pet(pet):
# #     pet.info()
# #     pet.make_sound()


# c= Cat('rocky',2)
# my_pet(c)
# d = Dog('bruno',3)
# my_pet(d)


        



# # def driver(car):
# #     car.drive()

# # class creta:
# #     def drive(self):
# #         print('creta is driving')

# # class mercedes: 
# #     def drive(self):
# #         print('mercedes is driving')

# # c = creta()
# # driver(c)    

# # m = mercedes()
# # driver(m)







###  GREETING IN DIFFERENT LANGUAGE:                   (   227  )

# def greet(language):
#     language.greeting()

# class English:
#     def greeting(self):
#         print('Hello')

# class French:
#     def greeting():
#         print('Bonjour') 

# E = English()
# greet(E)        





### MEASURING THE ANGLES :                            (   228  )

# class angle:
#     def __init__(self,deg):
#         self.degree = deg

#     def __add__(self,ang):
#         sum = angle(ang.degree +self.degree)
        
#         return sum
    
#     def __str__(self):
#         return 'degree '+ str(self.degree)
    
# a1 = angle(95)
# a2 = angle(30)
# a3 = a1+a2
# print(a3)    





###  POLICE ROBOT :                    (    229   )

# class Robot:

#     def __init__(self,name):
#         self.name =name

#     def say_hi(self):
#         print('Hi citti ') 

# class PoliceRobot(Robot):

#     def say_hi(self):
#         print('Hello police robot ')

# r = Robot('soniya')        
# r.say_hi()
# r1 = PoliceRobot('sonia')
# r1.say_hi()





# ###  DIIFERENT SHAPE CLASSES:                           (    230   )

# import math
# class shape:

#     def __init__(self,name):
#         self.name = name
#     def area(Self):
#         pass

# class rectangle(shape):

#     def __init__(self,l,b):
#         self.len = l
#         self.bre = b
#     def area(self):
#         return (self.len*self.bre)    

# class circle(shape):

#     def __init__(self,r):
#         self.rad = r
#     def area(self):
#         return (math.pi*(self.rad**2)) 

# rec = circle(7)
# print(rec.area())





### RATIONAL NUMBER :                           (   231  )

class rational:

    def __init__(self,p=1,q=1):
        self.p = p
        self.q = q

    def __add__(self,other):
        num = (self.p*other.q) +(self.q*other.p)
        deno = self.q*other.q
        sum = rational(num,deno)
        return sum

    def __sub__(self,other):
        r = rational()
        r.p = (self.p*other.q) - (self.q*other.p)
        r.q = self.q*other.q
        return r
    
    def __str__(self):
        return str(self.p) +'/'+str(self.q)
    
r1= rational(3,5)
r2=rational(5,7)
sum =r1+r2
print(sum)    
    














































