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

# L1= {'a':1,'b':2,'c':3}
# print(dict_rev(L1))




## PANGRAM PHRASE:                                                               (  165  )

# def pangram(phrase):                         
    
#     phr = set(phrase)
#     phr1 = 26
#     if len(phr) == phr1:
#         print('pangram')

#     else:
#         print('not a pangram')

                           #( OR )

# def pangram(phr):
#     phr1 = set(phr)
#     alphabet_list = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
#     for i in alphabet_list:
#         if i not in phr1:
#             return 'not pangram'
        
#     return ('pangram')

# print(pangram('abcdefghijklmnpqrstuvwxyzz88999.'))




## CASE COUNTING LETTERS:                                                           (  166  )

# def count(phrase):
    
#     low = 0
#     up = 0
#     for x in phrase:
#        Y= x.islower()
#        low = low + Y
#        z = x.isupper()
#        up = up + z

#     return low,up
# print(count('ANjdJD'))    

            
                

## MINIMUM VARIABLE NUMBER:                                                        (  167  )

# def minimum(*var , low_limit):

#     if low_limit is None:
#         return min(var)
#     else:
#         l = [x for x in var if x >= 0]
#         return min(l)
    
# print(minimum(1,2,3,4,-5,6,-1 ,low_limit=0))    





        





    

    



