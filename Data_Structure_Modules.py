### Top 3 Common Words:   

# from collections import Counter              

# import re

# l = '''Python is an easy programmers language.
#      Python syntax is like the English language.
#      Python language is easy to learn and adapt to comapared to java and C.
#      In Python language, the same task can be performed using fewer lines of code.
#      its easy learning and easy to code.'''

# text = l.split()

# c = Counter(text)

# print(c.most_common(3))





# ### Inventory :

# from collections import Counter

# inventory = Counter({'apples':50 , 'mango':100 , 'banana':120 , 'orange ':70})

# def update_inventory(orders):
#     inventory.subtract(orders)
    
# orders = Counter({'apples':10 , 'mango':12 , 'banana':15 , 'orange':50})
# update_inventory(orders)

# print(inventory)





# ###  Generate Bills with Subtotal: 

# from collections import Counter

# price = {'soap':50 , 'toothpaste':25 , 'shampoo':45.50 , 'toothbrush':15.99}

# def generate_bill(cart):
#      total =0
#      print('product     price    qty   total')
#      for product,qty in cart.items():
#          print (f'{product:10}  {price[product]:5} x {qty:2}   =  {price[product]*qty}')
#          total = total+price[product]*qty
#      print('total =',total)
# cart = Counter(soap=5 , toothpaste= 1,shampoo =2, toothbrush = 3)
# generate_bill(cart)








# SELECT 
#         t1.emp_id, 
#         t1.record_timestamp, 
#         (
#             SELECT t2.record_timestamp 
#             FROM employee_records t2 
#             WHERE t2.emp_id = t1.emp_id 
#             and day(t2.timestamp) = day(t1.timestamp)
#             AND t2.record_timestamp > t1.record_timestamp
#             ORDER BY t2.record_timestamp DESC
#             LIMIT 1
#         ) AS prev_timestamp
#     FROM 
#         employee_records t1


# t1
# -- 01-01-2024 08:00 747
# -- 01-01-2024 17:00 747
# -- 01-01-2024 08:00 748
# -- 01-01-2024 17:00 748

# t2                                    747 01-01-2024 08:00 01-01-2024 17:00
# -- 01-01-2024 08:00 747
# -- 01-01-2024 17:00 747
# -- 01-01-2024 08:00 748
# -- 01-01-2024 17:00 748







# from collections import Counter    (1)
# import re

# text = '''Python is an easy programmers language.
#      Python syntax is like the English language.
#      Python language is easy to learn and adapt to comapared with java and C.
#      In Python language, the same task can be performed using fewer lines of code.
#      its easy learning and easy to code.'''

# words = re.findall('\w+',text)

# count = Counter(words)

# print(count.most_common(3))



# from collections import Counter   (2)

# inventory = Counter({'apples':50 , 'mango':100 , 'banana':120 , 'orange ':70})

# def update_inventory(orders):
#     inventory.subtract(orders)


# orders = Counter({'apples':10 , 'mango':90 , 'banana':10 , 'orange ':40})
# update_inventory(orders)
# print(inventory)



# from collections import Counter   (3)

# price = {'soap':50 , 'toothpaste':25 , 'shampoo':45.50 , 'toothbrush':15.99}

# def generate_bill(cart):
#     total = 0
#     for item,value in cart.items():

#         print(item,price[item],'x',value,'=',price[item]*value)
#         total = total+price[item]*value
#     print(total)    
   


# cart = Counter(soap=5 , toothpaste= 1,shampoo =2, toothbrush = 3)
# generate_bill(cart)





##  BARBER SHOP QUEUE:   

from collections import deque

customer = deque()
  
def walk_in(cust):
    customer.append(cust)

def serviced():
    c=customer.popleft()
    print('serviced',c)
walk_in('john')

walk_in('smith')






























