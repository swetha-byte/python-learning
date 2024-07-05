## DIFF B/W 2NUMBERS:                                                    (  159  )

# def diff(a,b):

#     if abs(a-b) <= 5:
#         return True 
#     else:
#         return False
    
# print(diff(23,19))    
    


## MAX OF 3 NUMBERS:                                                    (  160  )

# def max(n1,n2,n3):
    
#     if n1>n2 and n1>n3:
#         return n1
#     elif n2>n3:
#         return n2
#     else:
#         return n3

# print(max(12,45,23))    



## PRINTING POSITIONAL MESSAGE:                                           (  161  )

# def msg(name,prof,/):

#     print('my name is' ,' '+ name +' ', 'i am a/an' + prof)

# msg('swetha','engineer')    



# ## PLANET NAMES:                                                          (  162  )

# def planet(id):
    
#     planet_names = {1:'mercury',2:'venus',3:'earth',4:'mars',5:'jupiter',6:'saturn',7:'uranus',8:'neptune',9:'pluto'}
#     if id in planet_names:
#         id2 = planet_names[id]
#         return id2

#     else:
#        return 'invalid_id'

# id1 = planet(int(input('enter id num : ')))
# print(id1)   



## scores ending with zero :                                                      (   163  )

# def scores(l):
#     s = 0
    
#     for i in l:
#        if i %10 == 0:
#            s =s+i

#     return s

# nums = scores([230,43,679,40,20])       
# print(nums)
                

       
## INVERTING A DICTIONARY :                                                        ( 164 )

# def dict_rev(l):

#     keys=l.keys()
#     val = l.values()
#     z = dict(zip(val,keys))  
   
#     return z   
# 
# 

# def dict_rev(L):
#     dict1 = {}
#     for key in L.keys():
#         dict1[L[key]] = key

#     return dict1  

L1= {'a':1,'b':2,'c':3}
print(dict_rev(L1))





    

    



