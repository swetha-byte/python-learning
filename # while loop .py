# # while......................

# count = 0
# while count < 15:
#    count = count + 1
#    print('hello' , count)

# n = int(input('enter a number : '))
# while n>0:
#     r = n%10
#     n = n//10
#     print(r)
    


# # MULTIPLICATION :.................................

# n = int(input('enter a number for multiplication table'))
# x = 0
# while x < 10:
#     x = x + 1
#     print(n , '*' , x , '=' , n * x)
    



# # #COUNTING THE NUMBER OF DIGITS IN A NUMBER:............................

# n = int(input('enter a number'))   4567
# i=0                          // 0
# while n>0:                   // true  true  true true  false
#     n=n//10                  //  456   45   4     0
#     i+=1                     //  i=1   i=2  i=3   i=4
#     print(i)                 //  1     2    3     4
# print(i)                     //                        4



# n= int(input('enter a number: '))
# i = 0
# while n>0:
#     n = n//10
#     i = i+1
# print(i)    
 

# #FIND SUM OF DIGITS IN A NUMBER:............................

# n = int(input('enter a number : '))   #  1234           
# i = 0                                            
# while n > 0:                    # true      true     true  true    false    1234
#     r = n%10                    # r = 4     3          2    1
#     n = n//10                   # n = 123   12         1    0
#     i = i+r                     # i= 4      7          9    10
# print(i)                        #                                   10


# #FIND SUM OF DIGITS IN A NUMBER:........................

# n = int(input('enter a number : '))   #  1234          
# i = 0                                            
# while n > 0:                    # true    true    true  true   false
#     n = n//10                   # 123       12     1      0
#     r = n%10                    # 3         2      1      0
#     i = i+r                     # 3         5     6     6
# print(i)                        #                                 6 


# #FIND SUM OF DIGITS IN A NUMBER:.......................

# a = (input('enter a number : '))   # 1234
# n_len = len(a)      
# i = 0 
# x = 0                                            
# while x < n_len:                    
#     i = i + int(a[x])               
#     x=x+1                     
# print(i)    


# a = '1234'
# len('1234') = 4
# a[0] = 1 a[1]= 2 a[2] = 3 a[3] = 4
 
# a[-1] = 4  a[-2] = 3 a[-3] = 2 a[-4] = 1




# # DISPLAY MULTIPLICATION FOR TABLE:......................

# n = int(input('enter a number multiplication: '))       
# i = 1 
# while i <= 10:
#     print ( n ,'*' ,i , '=' , n * i)
#     i = i + 1


# # COUNTING THE NUMBER OF DIGITS IN A GIVEN NUMBER:.................

# n = int(input('enter a number : '))           #56789
# i = 0                                         # 
# while n > 0 :                                 #true   true  true   true   true
#     n = n // 10                               #5678   567    56     5      0
#     i = i + 1                                 #i=1    i=2    i=3    i=4    i=5
# print (i)



### FIND SUM OF DIGITS IN A GIVEN NUMBER:..........................

# n = int(input('enter a number : '))
# i = 0
# while n > 0:
#     r = n % 10
#     n = n//10
#     i = i + r
# print (i)


## REVERSING A NUMBER :....................

# n = int(input('enter a number : '))         # n = 1234         
# rev = 0                                     # rev = 0         rev = 4           rev = 43        rev = 432
# while n > 0:                                #  true           true              true            true
#     r = n%10                                # 4                3                2               1
#     n = n//10                               # 123              12               1               0
#     rev = rev * 10 + r                      # 0 = 0*10 + 4     4*10+3=43        43*10+2=432     432*10 +1 = 4321     
# print(rev)

 
# ### check if a number is palindrome or not:.....................
 
# n = int(input('enter a number : '))
# m=n
# rev = 0
# while n>0:
#     r=n%10
#     n=n//10
#     rev = rev *10 + r
# if m == rev:
#     print ('palindrome')
# else:
#     print('not a palindrome')



## FIND SUM OF GIVEN NUMBERS AS INPUT:.................

# num_of_nos = int(input('enter number of numbers : '))        # 5        
# sum = 0                                                      # 0          6      7      13     19
# i = 0                                                        # 0          1      2       3      4
# while i < num_of_nos:                                        # true       true   true   true  true
#       n = int(input('enter a number : '))                    # 6          6      6       6      6
#       sum = sum+n                                            # 0=0+6      6+6=12      18      24     30
#       i =  i + 1                                             # 1          2      3       4      5
# print('sum of numbers is = ', sum)


# ## FIND SUM OF GIVEN NUMBERS AS INPUT:................. 

# num_of_nos = int(input('enter a numbers_of_nos : '))
# sum = 0
# i = 0
# while  num_of_nos>i :
#     n = int(input('enter a number : '))
#     sum = sum + n
#     i = i + 1
# print('sum of numbers', sum)   




# num_of_nos = int(input('enter a number : '))
# i=0
# while i < num_of_nos:
#     print('arun', i)
#     i = i + 1



# num_of_nos = int(input('enter a number : '))
# while num_of_nos > 0:
#     print('arun', num_of_nos)
#     num_of_nos =  num_of_nos - 1




# num_of_nos = int(input('enter a num_of_number : '))   ('PRACTICE SESSION')
# i=0
# sum=0
# while i < num_of_nos:
#       n=int(input('enter a number: '))
#       sum1= sum+n
#       sum2 = sum-n
#       i = i+1
# if n>0:
#     print(sum1)
# else: 
#     print(sum2) 


## FIND SUM OF GIVEN NUMBERS AS INPUT:.................
# num_of_nos = int(input('enter a number : '))
# posSum = 0
# negSum =0 
# i = 0
# while i < num_of_nos:
#     n = int(input('enter a number : '))
#     if n > 0:
#         posSum = posSum + n
#     else:
#         negSum = negSum + n
#     i = i + 1
# print('sum of positive numbers', posSum)   
# print('sum of negative numbers', negSum)   




### FIND SUM OF +VE ANG -VE NUMBERS:.............

# num_of_nos = int(input('enter a number : '))
# sum = 0
# diff = 0
# while num_of_nos > 0:
#     n = int(input('enter a number : '))
#     if n > 0:
#         sum = sum + n
#     else:
#         diff = diff + n
#     num_of_nos = num_of_nos -1
# print('pos sum', sum)
# print('neg sum', diff)


### FING MAXIMUM NUMBERS FROM GIVEN NUMBER:...................

# num_of_nos = int(input('enter a num_of_nos : ')) 5
# i=0
# hnum=0                             # 0    23        32         32
# while  i < num_of_nos:                  #  0        1          2                                
#     n= int(input('enter a number : '))  # 23        32         12
#     if n > hnum:                        # 23>0     32 > 23     12 > 32
#         hnum = n                        #   t          t       f
#     i=i+1                               # 1           2        3
# print('highest number', hnum)      



### CONVERT A DECIMAL NUMBER TO A BINARY NUMBER:.................

# n=int(input('enter a number : '))
# bin = 0
# while n>0:
#     r = n%2
#     n = n//2
#     bin = bin*10 + r
# rev = 0
# while bin > 0:
#     r =bin%10
#     bin = bin //10
#     rev = rev*10 + r

# print(rev)    


# # DECIMAL NUMBER TO A BINARY NUMBER:....

# n=int(input('enter a number : '))             #  n = 10
# bin = ''                                      #
# while n>0:                                    #
#     r = n%2                                   #0   1    0      1
#     n = n//2                                  #5   2    1      0
#     bin = str(r) + bin                        #0   10   101    1010

# print(bin)    



### GUESS A NUMBER between 1-10 :....................

# import random
# n = random.randint(1,10)
# guess = 0
# while guess != n:
#     guess= int(input('enter a number : '))
#     if guess > n:
#         print('number is greater')
#     elif guess< n:
#         print('number is smaller')
#     else:
#         print('you are right')        





































                                  