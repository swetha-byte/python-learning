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






### Barbershop Queue:

from collections import deque

customers = deque()

def walk_in(customers):