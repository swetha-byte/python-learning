# # Different ages:

# john = int(input('enter john age: '))
# smith = int(input('enter smith age: '))
# ajay = int(input('enter ajay age: '))
# if john > smith and john > ajay:
#     print('john is eldest')
# elif smith > ajay:
#     print('smith is eldest')
# else :
#     print('ajay is eldest')  
      



# # Discount amount:

# amount = int(input('enter amount: '))
# if amount <= 1000:
#     discount=amount *10/100 
#     print('discount of 10%: ',discount)
# elif 1000 < amount <= 5000:
#     discount=amount *20/100
#     print('discount of 20%: ',discount)  
# elif 5000 < amount <= 10000:
#     discount=amount *30/100
#     print('discount of 30%: ',discount) 
# elif 10000 < amount:
#     discount = amount *50/100
#     print('dicount of 50%: ',discount)      





# # Discount amount:

# amount = int(input('enter bill amount: '))
# if amount <= 1000:
#     discount=amount *10/100 
# elif 1000 < amount <= 5000:
#     discount=amount *20/100
# elif 5000 < amount <= 10000:
#     discount=amount *30/100
# else:
#     discount = amount *50/100
# discamount = amount - discount       
# print('pay' , discamount)



# # Displaying name of the day:
# day = int(input('enter day number : '))
# if day == 1:
#     print('sunday')
# elif day==2:
#     print('monday')   
# elif day ==3:
#     print('tuesday')   
# elif day == 4:
#     print('wednesday')   
# elif day == 5:
#     print('thursday')
# elif day ==6:
#     print('friday')
# elif day == 7:
#     print('saturday')
# else:
#     print('invalid day')



# LEAP YEAR OR NOT:

year = int(input('enter year : '))
if year % 4 == 0 and year % 100 != 0:
    print('leap year')
else:
    print('not a leap year')    