### SORTING THE LETTER OF A STRING:                           ( 78 )

# str1 = input('enter a string : ')
# s = sorted(str1)
# print(sorted(s))
# str2 = ''.join(s)
# print(str2)


### DISPLAYING DATA :....                                    ( 79 )

# item = input('enter a item : ')
# price = input('enter price : ')
# total_len = len(item)+len(price)
# print(total_len)
# dot = '.'*(25 - total_len)
# print(item+dot+price)


### CONFIRMING PASSWORD: .....                                ( 80 )
 
# pass1 = input('enter pw1 : ')
# pass2 = input('enter pw2 : ')
# if pass1 == pass2:
#     print('passwords are same')
# else:
#     print('please check for the case properly')    


### DISPLAY CREDIT CARD NUMBER : .....                            ( 81 )
\
# cardno = input('enter credit cardno : ')
# a = cardno[10:]
# print('*'*4, '*'*4, a)




# cardno = '1234-2345-1234-8493'
# a = cardno.split('3')
# print(a)

# s1 = 'xyz'
# s2 = ','

# print(s2.join(s1))

# a = 'swetha loves arun'
# # print(a.replace('loves','married'))
# print(a.rfind('love'))




# # CHALLENGING CREDIT CARD DETAILS :........                     

# cardno = input('enter a number : ')
# print(cardno)


###  SORTED , ITEM PRICE , PASSWORD :...................................

# str1 = input('enter a string : ')
# ss = sorted(str1)
# print(sorted(str1))
# str2 = ' '.join(ss)
# print(str2)

# item = input('enter the item : ')
# price = input('enter price : ')
# total_len = len(item)+len(price)
# print (total_len)
# total = (30 -total_len)*'.'
# print(item+total+price)

# pw1 = input('enter password: ')
# pw2 = input('enter confirm password: ')
# if pw1==pw2:
#     print('''yes you have same pw's''')
# else:
#     if pw1.casefold() == pw2.casefold():
#        print('please check the password')
#     else :
#        print('you enterd incorrect pwd')    


        
###  CREDIT CARD DATAILS :..............   

# cardno = input('enter cardno: ')
# last_digits =cardno[15:]
# print(last_digits)
# print('*'*4 , '*'*4 , '*'*4 , last_digits)

             # (OR) #

# cardno = input('enter a cardno : ')
# last_digits = cardno[15::]
# stars = ('*'*4 + ' ') * 3
# print(stars + last_digits)


### NAME DOMAIN NAME FROM Email :............                ( 82 )

# user_name = input('enter user_name : ')
# domain_name = input('enter domain_name : ')
# print(user_name + '@'+ domain_name)
    
             # (OR) #
 
### FIND USER_ID & DOMAIN_NAME FROM EMAIL ADDRESS:.............

# emailid = input('enter emailid: ')
# atrate = emailid.find('@')
# print(atrate)
# print('user_id :',emailid[:atrate])
# print('doamin_name :',emailid[atrate+1:])




### CONVERTING STRING TO PALINDROME : .................          ( 83 )
# 1 , CHECKING A STRING IS A PALINDROME

# name1 = input('enter name1: ')
# name2 = name1[::-1]
# print(name1,name2)
# if name1 == name2:
#     print('its a palindrome')
# else :
#     print('not a palindrome')    


### FIND DAY , MONTH , YEAR : .....................         ( 84 )

# mydate = input('enter date in dd/mm/yyyy format : ')
# l = mydate.split('/')
# print('day:',l[0])
# print('month:',l[1])
# print('year:',l[2])



### CHECKING IF TWO STRINGS ARE ANAGRAM:.................         ( 85 )
 
# s1 = input('enter string1: ')
# s2 = input('enter string2: ')
# if len(s1)!= len(s2):
#     print('not anagram')
# else :
#     for x in s1:
#         if x not in s2:
#             print('not anagram')  
#             break; 
#     else :
#        print('anagram')    



### REARRANGE : LowerCase then UpperCase:..... .......          ( 86 )
 
# string = 'aBcDEFghiJkL'
# SS = sorted(string)
# print(SS)
# lower = SS.islower()
# upper = SS.isupper()
# print(lower+upper)
   
                         #( OR )

# str1 = 'AJjnDfdFgv'
# lower = ''
# upper = ''
# for x in str1:
#     if x.islower():
#         lower += x
#     else:
#         upper += x
# str2 = lower + upper    
# print(str2)        



### REMOVING PUNCTUATIONS:.................          ( 87 )

# punct = '([[{*!"£$%^&**(().@#<>?_)}]])'
# s1 = '[my_python@gmail.com]'
# s2 = ''
# for x in s1:
#     if x  not in punct:
#         s2 = s2 + x
# print(s2)