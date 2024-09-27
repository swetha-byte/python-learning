# import csv
# f = open('employee.csv','r')
# csv_reader = csv.reader(f)

# for row in csv_reader:
#     print(row)




# import csv

# f = open('employee.csv','r')
# csv_read = csv.reader(f)

# next(csv_read)

# sales = []
# for row in csv_read:
#     sales.append(int(row[2]))

# print(sales)  
# print('min',min(sales))
# print('max',max(sales))  



## CREATING A CSV FILE USING WRITER:

# import csv

# covid = [('country','doses','people','percentage'),
#          ('india','186cr','84.1cr',61),
#          ('china','330cr','124cr',88.1),
#          ('us','56.8cr','21.9cr',66.4),
#          ('brazil','42.4cr','16.2cr',76.4)
#          ]

# f = open('covid.csv','w',newline='')
# wrtr = csv.writer(f)

# for t in covid:
#     wrtr.writerow(t)

# f.close()    


## CSV DICTIONARY WRITER:
import csv

covid = [
         {'country':'india','doses':'186cr','people':'84.1cr','percentage':61},
         {'country':'china','doses':'330cr','people':'124cr','percentage':88.1},
         {'country':'us','doses':'56.8cr','people':'21.9cr','percentage':66.4},
         {'country':'brazil','doses':'42.4cr','people':'16.2cr','percentage':76.4}
         ]

f=open('coviddict.csv','w',newline='')
fields = ['country','doses','people','percentage']

wrtr = csv.DictWriter(f,fields)
wrtr.writeheader()

for d in covid:
    wrtr.writerow(d)

f.close()
