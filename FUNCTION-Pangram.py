
## PANGRAM CHANGE: ##                                                             (  165  )


# def pangram(phrase):
    
#     letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
#     phr = set(phrase)
    
#     if len(phr) >=  len(letters):
#         return True
#     else:
#         return False
    
# p1 = pangram('the quick brown fox jumps over the lazy dog')
# print(p1)   


## CASE COUNTING LETTERS : ##                                                            (  166  )

# def count(phrase):
    
#       low=0
#       up =0 
#       for i in phrase:
#           if i.islower():
#                low = low +1
               
#           else:
#                up= up +1

#       return low , up  

# print(count('ABdcjSAKJE'))          



###     MINIMUM VARIABLE NUMBER:                                                       (  167  )

# ##  min (1,5,7,-5,6)  ...............  # (return -5)

# def min( *val, low_limit= None):
#     if low_limit is None:
#         return min(val1)
#     else:
#         l=[x for x in val if x >= low_limit ]
#         return l
    
# val1 =min(1,5,4,7,-5,4) 
# print(val1)   



##  PASCAL'S TRAINGLE:                                                       (  168  )

# def pascal(n):
#     r = [1]

#     for i in range(n):
#         print(r)
#         tr = [0]+r
#         r = r +[0]
#         nr = [ x+y for x,y in zip(r,tr)]
#         r = nr

# pascal(6) 



### FLATTEN A NESTED LOOP :                                                 (  169  )

def flatten(l):
    for e in l:
        if hasattr(e , '__iter__'):
            yield from flatten(e)
        else:
            yield e

f = flatten([1,2,3,[2,4,5,[1,2,3],3,9],7])
print(next(f))
print(next(f))
print(next(f))           
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))



       
