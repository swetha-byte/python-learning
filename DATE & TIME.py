###  MONTHS STRATING FROM MONDAY :             (  247  ) 

# from datetime import*

# import datetime
# year = int(input('enter year : '))

# monday = 0
# for month in range(1,13):     
#     dt = datetime.date(year,month,1)
        
#     if dt.weekday() == 0:
#         monday += 1
#         print(month)

# print('number of months starting with monday :',monday )           





###  CODE EXECUTION TIME:            (   248  )

# import time

# start_time =time.time()

# for i in range(100000000):
#     pass

# end_time = time.time()

# ex_time = end_time - start_time

# print(ex_time)






# ###   STRING TO OBJECT DATE:           (  249  )

# import datetime

# str_date = input('enter date in the form of DD-MM-YYYY : ')

# d,m,y = str_date.split('-')
# d1 = datetime.date(int(y),int(m),int(d))
# print(d1)





# ###  CALCULATE AGE:              (   250  )

# from datetime import date

# def age(dob):

#     today = date.today()
#     years = today.year - dob.year

#     if (today.month , today.day) < (dob.month , dob.day):
#         years -= 1

#     return years
  
# print('Age:',age(date(1998,4,11)))






###  LAST THURSDAY's Date:      ( 251 )

from datetime import date
 
def prev_day(day):
    week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    tw_day = date.today()
    day_wk = date.weekday(3)
    diff = day_wk - tw_day
    return diff

days = prev_day('Thursday')
print(days)

      












