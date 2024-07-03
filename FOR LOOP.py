# msg = 'hello'
# for x in msg:
#     print(x)


### DISPLAY MULTIPLICATION TABLE FOR A GIVEN NUMBER:...............

# n = int(input('enter a number : '))

# for i in range(1,11):
#     print(n ,'* ' , i , '=' , n * i)
    


###  FIND FACTORIAL OF A GIVEN NUMBER :..................

# n = int(input('enter a number : '))
# fact = 1
# for i in range(1 , n+1):
#     fact = fact * i
#     print (fact)



### PRINT N TERMS OF AP series :.................

# n = int(input('enter nos_of_terms : '))
# a = int(input('enter a initial nos: '))
# d = int(input('common differrence : '))
# for i in range(a , a +n*d , d):
#     print (i)



### PRINT N TERMS OF FIBONACCI SERIES :............

# a = int(input('enter 1st number : '))
# b = int(input('enter 2nd number : '))
# n = int(input('enter no_of_terms : '))
# for i in range(n):
#     print (a)
#     c=a+b
#     a=b
#     b=c




### FIND THE FACTORS OF A NUMBER:

# n = int(input('enter a number :'))
# for i in range(1, n):
#     if n % i ==0:
#       print('factors are' , i)



### CHECK IF A NUMBER IS PRIME OR NOT:...........

# n = 1
# no_of_factors = 0
# for i in range(1 ,n+1):
#     if n%i == 0:
#         no_of_factors = no_of_factors+1
# if no_of_factors == 2:
#    print(n ,'is prime number')
# else:
#     print(n ,'is not a prime  number')  



# x=int(input('Enter a number:'))
# num = 0
# for n in range(1,x):
#     no_of_factors = 0
#     for i in range(1 ,n+1):
#         if n%i == 0:
#             no_of_factors = no_of_factors+1
#     if no_of_factors == 2:
#         print(n ,'is prime number')   
#         num = num + 1
# print('Number of prime numbers between 1',x,' is', num)


# for i in range(1,20):
#     if(n%4 == 0):
#         print('even',n)


def isPrime(n):
    no_of_factors = 0
    for i in range(1 ,n+1):
        if n%i == 0:
            no_of_factors = no_of_factors+1
    if no_of_factors == 2:
        return 'true'
    else:
        return 'false' 
    
x = isPrime(17)
print(x)


     
