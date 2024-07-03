# write a program to find the sum of the digits in a given number:
# num = int(input('enter a number : '))         # 1234     
# i = 0                                         # i = 0
# while i < num:                                # t
#     r = num %10                               # 4
#     num = num//10                             # 123  
#     i = i +r                                  # 4     
# print(i)


## Reversing a number:
# num = int(input('enter a number: '))
# rev = 0
# while num>0:
#     r = num % 10
#     num = num // 10
#     rev = rev *10 + r 
# print(rev)


## Palindrome :
# num = int(input('enter a number : '))          
# m = num                                     
# rev = 0 
# while num >0 :
#     r = num%10
#     num = num// 10
#     rev = rev *10 +r
# if rev == m:
#     print('you are a genious')
# else:
#     print('you are an idiot')        


## even number (0-50) using for loop :
i = 0
for i  in range(31,60,2):
        print(i)
    
