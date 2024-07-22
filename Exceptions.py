# ###  NEGATIVE AGE: ###                                   (  187  )

# def stage(age):

#     if age < 0:
#         raise 'NegativeAgeError'
#     elif  age <= 13:
#         return 'kid'
#     elif age <=19:
#         return 'teen'
#     elif age < 50:
#         return 'young'
#     else:
#         return 'old'
   

# age = int(input('enter age: '))                                           

# try:
#     age1 = stage(age)
#     print(age1)
# except:
#     print('negative age exception')    




# class NegativeAgeException(Exception):                    (   187-a   )
#     pass

# def stage(age):

#     if age < 0:
#         raise NegativeAgeException('Age should not be negative')
#     elif  age <= 13:
#         return 'kid'
#     elif age <=19:
#         return 'teen'
#     elif age < 50:
#         return 'young'
#     else:
#         return 'old'
   

# age = int(input('enter age: '))

# try:
#     age1 = stage(age)
#     print(age1)
# except NegativeAgeException as e:
#     print(e)   






# ###  ACCOUNT BALANCE ###                                        (  188  )

# class AccountBalanceException(Exception):
#     pass

# balance = 10000

# def Withdraw(amt):
#     global balance
#     WD = balance - amt
    

#     if WD <= 5000:
#         raise AccountBalanceException('minimum balance should be 5000')
#     else:
#         print(WD)
    

# try:
#     Withdraw(4000)
# except AccountBalanceException as msg:
#     print(msg)
    




# class AccounbalanceException(Exception):                            # (   188-a  )
#     pass

# balance=10000

# def withdraw(amt):
#     global balance

#     if balance - amt < 5000:
#         raise AccounbalanceException('minimum amt should be 5000')
#     else :
#         b = balance-amt
#         print('Remaining amt is' , b)

# try:
#     amt = int(input('enter amount: '))
#     withdraw(amt)
# except AccounbalanceException as e:
#     print(e)






### SIMPLE CALCULATOR :                                              (  189  )

# class InvalidFormulaException(Exception):
#     pass

# def evaluate(formula):
#     f = formula.split()

#     if f[1] == '-' or f[1] == '+' or f[1] == '*' or f[1] == '//':
#         op1 = int(f[0])

#         print(f)
#     else :
#         raise InvalidFormulaException('enter the correct operators')

# try:
#     evaluate(5-2)
# except InvalidFormulaException as msg:
#     print(msg)




#   EX:1  #

class ZeroDivisionError(Exception):
    pass 
def div(a,b):

    try:
        c = a // b
        return c
    except ZeroDivisionError as msg:
        print(msg)
    # finally:
    #     print('finally block')

# a = int(input('enter first num: '))
# b = int(input('enter second num: '))
z = div(10,0)

print(z)

    