# birthdays = {                                       ( 139 )
#     'Sachin' : '10 /04 /2003' ,
#     'Charlis': '24 / 05 / 1997',
#     'Trump'  : '13 /07/2000',
#     'Donald' : '11 / 10/2020',
#     'Tina'   : '19/11/2024'}
# name = str(input('enter a name : '))
# if name in birthdays:
#     print(name , birthdays[name])
# else:
#     print('name is not found')
    

# FIND LONGEST AND SHORTEST MEANING IN A DICT:        ( 140 )
# dict1 = { 
#     'piece':'a portion of an object or of material, produced by cutting, tearing, or breaking the whole.',
#     'cut'  :'make an opening, incision, or wound in (something) with a sharp-edged tool or object',
#     'visit':'an act of going to see a person or place as a guest, tourist, etc.',
#     'with' :'accompanied by (another person or thing).',
#     'small':'of a size that is less than normal or usual.',
#     'large': 'accompanied by (another person or thing).'}
# keys =list(dict1.keys())
# values = list(dict1.values())
# lens = [len(x)  for x in values]
# print(max(lens), min(lens))



 
# dict1 = {1:2,2:4,3:9,4:16,5:25}                    { 1 }
# print(dict1)
# print(type(dict1))

# dict1 = dict(((1,2),(2,4),(3,9),(4,16),(5,25)))     { 2 }
# print(dict1)
# print(type(dict1))


# dict1 = [1,2,3,4,5,6]                               { 3 }
# dict2 =[1,4,9,16,25,36]
# print(dict(zip(dict1,dict2)))

             ## ( OR ) ##

# dict1 = [1,2,3,4,5,6]                               
# dict2 =[1,4,9,16,25,36]  
# dict3 = {}
# for i in range(len(dict1)):
#      dict3[dict1[i]] = dict2[i]
# print(dict3)     

# dict4 = [23,43,54,67,89,86]                        { 4 }
# dict_result = dict(enumerate(dict4))
# print(dict_result)

           ####

# d1 = [1,2,3,4]
# d2 = ['a','b','c','d']
# d3 = {x:y for x,y in enumerate(d1)}
# print(d3)

# ## COUNTRIES NAMES                               ( 141 )
# countries = {}
# for x in range(5):
#     name = input('enter the country name ')
#     if name[0].upper() not in countries:
#         countries[name[0].upper()]=[name]
#     else:
#         countries[name[0].upper()].append(name)
# print(countries)            
       


# ### ROMAN TO INTEGER:                           ( 142 )
# roman = {
#     'I'  : 1,
#     'V'  : 5,
#     'X'  : 10,
#     'L'  : 50,
#     'C'  : 100,
#     'D'  : 500,
#     'M'  : 100 }
# number = input('enter a roman num in uppercase: ')
# for x in roman:
#     if number[0] > number[1]:
#         number[0]-number[1]
#     else:


### STUDENT DETAILS :                        ( 143 )

# student = {}

# for i in range(3):
#     name = input('enter name : ')
#     rollno = input('enter rollno : ')
#     dept = input('enter dept : ')
#     student[name]={'Rollno':rollno , 'Name':name,'Dept':dept}
# print(student)    











#                       #### (PRACTICE) ####
# # 139    BIRTHDAY OF A PERSON :

# birthdays = {
#     'Swetha' : '11/04/1998',
#     'Arun'   : '10/04/1994',
#     'Dolly'  : '29/03/2000',
#     'Rahul'  : '10/07/2006' }

# name = str(input('enter a name : '))

# if name in birthdays:
#     print(name ,birthdays[name] )
       
# else:
#     print('name is not found')    




birthdays = {
    'Swetha' : '11/04/1998',
    'Arun'   : '10/04/1994',
    'Dolly'  : '29/03/2000',
    'Rahul'  : '10/07/2006' }
name = input('enter a name : ')
if name in birthdays:
    print(name ,birthdays[name])
else:
    print('name is not found')    
















