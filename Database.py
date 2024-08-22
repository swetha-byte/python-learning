
# import sqlite3

# conn = sqlite3.connect('University.db')

# cur = conn.cursor()

# dept = int(input('Enter Deptno: '))
# dname = input('Enter dname: ')

# rollno =int(input('Enter roll num: '))
# name = input('Enter student name: ')
# city = input('Enter city: ')
# Deptnum = int(input('Enter deptnum: '))



# cur.execute(f'insert into Dept VALUES ({dept},"{dname}")' )
# cur.execute(f'insert into students values({rollno},"{name}","{city}",{Deptnum})')

# cur.execute('Create table Dept(deptno , dname)')
# cur.execute('Create table Students(rollno integer primary key ,name text, city text, Deptno integer, foreign key(Deptno) references dept(deptno) )')

# conn.commit()

# cur.close()

# conn.close()









######################################################################


# import sqlite3

# conn = sqlite3.connect('university.db')

# cur = conn.cursor()

# rows = cur.execute('select * from Dept')
# rollno = rows.fetchall()

# print('Roll  Name')

# for t in rollno:
#     print(t[0] ,'  ', t[1])

# cur.close()

# conn.close()





#####################################################################################


# import sqlite3

# conn = sqlite3.connect('university.db')

# cur = conn.cursor()

# cur.execute(" update students set city='Bhopal' where rollno = 15 ")

# conn. commit()

# cur.close()

# conn.close()


























