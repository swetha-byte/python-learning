###  NEGATIVE AGE: ###

def stage(age):

    if age < 0:
        raise 'NegativeAgeError'
    elif  age <= 13:
        return 'kid'
    elif age <=19:
        return 'teen'
    elif age < 50:
        return 'young'
    else:
        return 'old'
   

age = int(input('enter age: '))

try:
    age1 = stage(age)
    print(age1)
except:
    print('negative age exception')    
