# from datetime import*
import datetime
year = int(input('enter year : '))

monday = 0
for month in range(1,13):     
    dt = datetime.date(year,month,1)
        
    if dt.weekday() == 0:
        monday += 1
        print(month)

print('number of months starting with monday :',monday )           



























