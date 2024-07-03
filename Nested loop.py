### PRINT PRIME NUMBERS FOR 1-100:
# a number which has only 2 factors


# n = int(input('Enter a number:'))
# totalp=0
# for num in range(1,n):
#     no_of_factors=0
#     for i in range(1,num+1):
#         if(num%i == 0):
#             no_of_factors = no_of_factors + 1
#     if(no_of_factors == 2):
#         print(num, 'is a prime number')
#         totalp = totalp+1
# print('Number of prime numbers', totalp)


                                        ##### STEPS #####

# n = int(input('enter a  number: '))
# for n in range(1,n+1):
#       if n%2 == 0:
#             print(n)





# n =int(input('enter a number : '))
# factors = 0
# for n in range(1,n+1):
#     if n%2==0:
#         print(n)
#         factors = factors +1
# print('no_of_factors for' , n ,'is' , factors)                





for n in range(1,101):
    factors = 0 
    for i in range(1,n+1):
        if n%i==0:
           factors = factors +1 
    if factors == 2:
           print (n)                   



# n = int(input('Enter a number:'))
# totalp=0
# for num in range(1,n):
#     no_of_factors=0
#     for i in range(1,num+1):
#         if(num%i == 0):
#             no_of_factors = no_of_factors + 1
#     if(no_of_factors == 2):
#         print(num, 'is a prime number')
#         totalp = totalp+1
# print('Number of prime numbers', totalp)


