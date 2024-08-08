# practice
### concatenation:   (joing strings by using '+')
 
# s1 = 'hello'                ( 1 )
# s2 = 'world'
# print(s1+' '+ s2)

# s1 = 'hello'                ( 2 )
# s2 = '15'
# print(s1+s2)

# s1 = 'hello'
# s2 = str(15)
# print (s1+'.'+s2)


### Repetition:.....         (multiplying a string)

# s = 'hello'
# x= ' '.join([s]*3)
# print(x)

# def multiply_string_with_spaces(s, n):
#     return ' '.join([s] * n)

# result = multiply_string_with_spaces("abc", 3)
# print(result)
 

### INDEXING: .......               ( )
 
# s1 = 'hello world'
# print(len(s1))
# print(s1[4:8])
# print(s1[:9])
# print(s1[:])
# print(s1[:-3])
# print(s1[:-1])
# print(s1[-7:-2])
# print(s1[2:7])
# print(s1[-11:])
# print(s1[-11:-4])
# print(s1[-10:-3:2])
# print(s1[-10::])
# print(s1[-11::3])
# print(s1[-8::-3])       # count fron left
# print(s1[-8::3])        # count from right



### string methods :    
# find()
# s = 'Learning Python'
# print(len(s))
# print(s.find('l'))
# print(s.find('g'))
# print(s.find('n',10))
# print(s.find('Lea'))
# print(s.rfind('n',5,8))

### joining and spliting:...........  
# s = 'a=v=d=f=d=e=l'
# print(s.replace('=',','))
# print(s.replace('f','g'))
# print(s.replace('=',''))

# s1 = 'abcd'                       #( joining)
# s2 = '/'
# print(s2.join(s1))

s1 = 'hello=world'
# print(s1.split())
print(s1.split('='))

arun is a good boy
