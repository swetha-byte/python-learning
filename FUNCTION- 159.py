## DIFFERENCE B/W TWO NUMBERS: ##              ( 159 )

# def diff(a,b):
    
#     if (a-b) <= 5:
#         return True
#     else:
#         return False

# res = diff(12,9)
# print(res)     


# def filter1(function,list):
#     x=[]
#     for item in list:
#             x.append(item)
#     return x

# L = [1,2,3,4,5]
# def even(x):
#     if x %2 == 0:4
#         return x
# f = filter(even , L)
# for i in f:
#     print(i)  


# def additem (item , l=[]):
#     l.append(item)
#     return l
# l1 =[1,2,3,4]
# additem(5,l1)
# print(l1)
# print(additem(33))


### MAXIMUM OF 3 NUMBERS :                     ( 160 )

# def max(a,b,c): 

#     if a > b and a > c :
#         return a 
#     elif b > c :
#         return b
#     else:
#         return c
# print(max(23,45,63))    



# def fun(** KWargs):
#    print(KWargs)
# fun(name = 'abd',age = 500 , address ='somewhere')

# def fun(*args):
#     print(args)
# fun(10 ,12.4, True,'john')    

# g = 10 
# print('ot1:', g)

# def fun(a,b):
#     c = a+b
#     global g
#     g=20
#     print('local',c)
#     print('global',g)

# fun(4,8)  
# print('ot2',g)  
    

## WRITE A FUNCTION TO PRINT 'HELLO WORLD':                        ( 1 )

# def greet(name,last_name):
#       print('hello',name,'is your lastname',last_name)    

# greet('swetha','peddamma')


## WRITE A FUN THAT RETURNS SGUARE OF A NUMBER:                     ( 2 )

# def squ(a):
#     return a**2
# num =squ(2)
# print(num)


## 

# def num(a):
#     if a >=10 and a<=20:
#         print(a,'you are in range')
#     else:
#         print(a,'you are not in range')   

# num(21)  



## PRINTING POSITIONAL MESSAGE : ###                                   ( 161 )

# def msg(name,proffession,/):
#     print('My name is',name,'I am a/an',proffession)        #print('My name is'+name+'and I am a/an'+proffession)

# msg('swetha' ,'civil engineer' )    


###   PLANET NAMES:  ###                                               ( 162 )

# def planet(id):
#     planet_names = {1:'mercury',2:'venus',3:'earth',4:'mars',5:'jupiter',6:'saturn',7:'uranus',8:'neptune',9:'pluto'}
#     if id > 0 and id <= 9:
#         print(planet_names[id])

#     else:
#        print('invalid id')

# id = int(input('enter planet id '))
# planet(id)




##  SCORES ENDING WITH ZERO : ##                                        ( 163 )

# def sum(L):
    
#     s = 0
#     for x in L:
#         if x %10 == 0:
#             s = s +x
#     return s

# L = [100,232,400,675,300,200]
# print(sum(L))




# ## INVERT A DICTIONARY : ##                                             ( 164 )

# def invert(dict):
#     new_dict = {}
    
#     for key , value in dict.items():
#         if value not in new_dict:
#             new_dict[value] =key
#         else:
#             new_dict[value].append(key)

#     return new_dict

# dict = {'a': 10 , 'b': 20 , 'c' : 30, 'd' : 40, 'e' : 50}
# print(invert(dict))

       
                    #(  OR  )


def invert(dict):
     newd = {}

     for key,value in dict.items():
        newd[value] = key
        
     return newd

dict = {'a': 10 , 'b': 20 , 'c' : 30, 'd' : 40, 'e' : 50 , 'f': 60}  
print(invert(dict))
   


        













     
       


