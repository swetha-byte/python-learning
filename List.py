# list1 = [1,2,3,4,5]
# i = 0
# while i < len((list1)):
#     print(list1[i])
#     i = i +1

# list1 = int(input('enter a list '))
# rev = 0
# while len((list1))>0:
#     r = list1% 10
#     list1 = list1 // 10
#     rev = rev *10 + r
#     print(list1[i])
#     print(rev)



# my_list = [1, 2, 3, 4, 5]
# reversed_list = []

# # Initialize an index at the last element of the list
# index = len(my_list) - 1

# # Loop until the index is valid (i.e., non-negative)
# while index >= 0:
#     reversed_list.append(my_list[index])
#     index -= 1

# print(reversed_list)  # Output: [5, 4, 3, 2, 1]

# days = int(input('enter num_of_days = '))
# hours = []
# for i in range(days):
#     working_hrs = int(input('enter working_hrs in a day = '))
#     hours.append(working_hrs)
# print(hours)
# sum = 0 
# for i in range(len(hours)):
#     sum = sum+hours[i] 
# print(sum)
# per_hr_cost = int(input('enter cost_per_hr = '))
# salary = sum* per_hr_cost
# print(salary)       


## list1 = [100,200,300,400,500]                             (1)
# list1.reverse()
# print(list1)


## CONCATENATE TWO LISTS INDEX-WISE :                         (2)
# list1 = ['m','na','i','ke']
# list2 = ['y','me','s','lly']
# l3 = []
# for i in range(len(list1)):
#     j = list1[i]+list2[i]
#     l3.append(j)
# print(l3)    


## TURN EVERY ITEM OF A LIST INTO ITS SQUARE:                 (3)
# l1 = [1,2,3,4,5,6,7]
# l2 = []
# for i in range(len(l1)):           ## for i in l1:                    
#     j = l1[i] *l1[i]                # l2.append(i*i)
#     l2.append(j)                    # print(l2)
# print(l2)    
     
    ### (OR)###
# l1 = [1,2,3,4,5]
# l2 = [x**2 for x in l1]
# print(l2)
             
### CONCATENATE TWO LIST IN A SPECIFIC ORDER :                (4)
# l1 = ['hello ' , 'take ']
# l2 = ['dear', 'sir']
# l3 = []
# for i in l1:
#  for j in l2:
#     k = i+j
#     l3.append(k)
# print(l3)   


# ### ITERATE BOTH LISTS SIMULTANEOUSLY :                       (5)
# list1 = [10,20,30,40,50]
# list2 = [100,200,300,400,500]
# list2.reverse()
# l3=[] 
# for i in  range(len(list1)):
#     print(list1[i] , list2[1])



# l1 = [1,2,3,4,5]
# for i in l1:
#     print(i)    



# ### REMOVE EMPTY STRING:                                      (6)
# l1 = ['MIKE', '', 'EMMA', '','KELLY', '']
# count = l1.count('')
# for x in range(count):
#     l1.remove('')
# print(l1)


# remove - fn/method - input - value 
# range - function/method input - number - output [0,1,2], start,end,increment  range(6) range(0,6,1)  range(6,12) [6,7,...11]
# len - function - input - list/string - output - length 


## DUPLICATES 
# l1 = [ 1,2,3,5,4,2,3,4,6]
# l2 = [ ]
# for x in l1:
#     if x not in l2:
#        l2.append(x)
# print(l2)

# l1 = [1,4,3,2,4,5,3,4,5,6,7,8,9,3,5,5]
# l1.sort()
# print(l1)
# for x in l1:
#     while l1.count(x) != 1 :
#        l1.remove(x)
# print(l1)       

### CONCATENATE ALL INTEGERS FROM A LIST TO A SINGLE NUMBER :       
# l1 = [3,5,10,7,11,12]
# str1 = ''
# for x in range(len(l1)):                   ## for x in l1:
#     str1 =str1 + str(l1[x])                 # str1 = str1+ str(x)
# print(str1)                                 # print(int(str1))


# arun = ['pizza','nuggets', 'hotdogs', 'noodles', 'pasta', 'burger'] 

# swetha = ['burger', 'hotdogs', 'noodles', 'pasta', 'nuggets', 'pizza'] 

# take a variable arun_index = 10
# take another variable swetha_index = 10
# loop through one of the list(arun)
#     now find the indexes of each element
#         compare if sum of indexes < sum of two indexes

# l1 = []
# for x in range(10):
#     l1.append(x)
# print(l1)

# l1 = [x for x in range(10)]
# print(l1)
# l1  = [x**2 for x in range (1,11,2)]
# print(l1)
# l1 = [x for x in (4,2,6,7,8,9) if x%2 == 0]
# print(l1)

# l1 = [12,3,4,33,4,4,123]
# str1 = ''
# for x in l1:
#     str1 = str1+str(x)
# print(str1)    

# ### OVERLAPPING ELEMENTS IN TWO LIST:                    ( 114 )
# l1 = [1,2,3,4,5,55,66,77,33,55,98]
# l2 = [66,12,33,2,4,6,7,22,98]
# l3 = []
# for x in l1:                      #
#     if x in l2:
#         l3.append(x)   
# print(l3)      


# ### FIND THE NUMBER OF OCCURRENCES OF EACH ITEM:           ( 115 )
# l1 = [ 'A' , 'E','D','J','T','A','E','A','B','E','J','D','A','E','F']
# result = []
# for x in l1:                                 #'A'
#     if x  not in result:                     # 'A'
#         result.append(x)                 # 
#         count = l1.count(x)
#         result.append(count)
# print(result)                


# l1 = [ 'A' , 'E','D','J','T','A','E','A','B','E','J','D','A','E','F']
# l2 = []
# for x in l1:
#     if x not in l2:
#         l2.extend([x , l1.count(x)])
# print(l2)


# code = ['._','_...','_._.','_..','.','.._.','_ _.','....','..','._ _ _']
# text = 'deface'
# morse_code = ''
# for x in text:
#     morse_code=morse_code + code[ord(x)-97] +' '
# print(morse_code)

# l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# l2 = [[5,6,7,8],[2,4,5,6],[5,3,1,8]]
# l3 = []
# for i in range(3):
#     s = []
#     for j in range(4):
#         s1 = l1[i][j]+l2[i][j]
#         s.append(s1)
#     l3.append(s)
# print(l3)

# l1 =[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# l2 =[]
# for i in range(4):
#     s = []
#     for j in range(3):
         
#          s.append(l1[j][i])
#     l2.append(s)     
# print(l2)

# food = ['pizza','burger','pasta','hotdog','nuggets','noodles']
# letter = str(input('enter a letter : '))
# for x in food:
#     if x.startswith(letter):
#         print(x)













