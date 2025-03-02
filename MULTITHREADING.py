
# USING FUNCTION:

# from threading import*
# from time import*

# def display():
#     for i in range(65,91):
#         print(chr(i))
#         sleep(1)

# t = Thread(target=display)
# t.start()

# for i in range(65,91):
#     print(i)
#     if(i==70):
#         t.join()
#     sleep(1)
# sleep(3)
# print("arun")
# t.join()
# sleep(2)

# print("kumar")



# ## USING CLASS:

# from threading import*
# from time import*

# class Alphabets(Thread):
#     def run(self):
#       for i in range(65,91):
#         print(chr(i))

# t = Alphabets()
# t.start()

# for i in range(65,91):
#     print(i)

# t.join()    




###  THREAD SYNCHRONISATION USING MUTEX:

# from threading import*
# from time import*

# def display(str1):
#     l.acquire()

#     for i in str1:
#         print((i))
#     l.release()

# l = Lock()
# t1 = Thread(target=display,args=('HELLO WORLD',))
# t2 = Thread(target=display,args=('you are welcome',))
# t1.start() 
# t2.start()

# t1.join()
# t2.join()  




# ###  THREAD SYNCHRONISATION USING SEMAPHORE:

# from threading import*
# from time import*

# def display(str1):
#     l.acquire()

#     for i in str1:
#         print(i)
#         sleep(0.2)
#     l.release()

# l = Semaphore(1)

# t1 = Thread(target=display,args=('HELLO WORLD ',))
# t2 = Thread(target=display,args=('you are welcome ',))
# t3 = Thread(target=display,args =('LEARNING PYTHON ',))

# t1.start()
# t2.start()
# t3.start()

# # for i in range(65,91):
# #     print(i)

# t1.join()
# t2.join()
# t3.join()




###  INTER PROCESS COMMUNICATION:                         (   FLAG , LOCK  )

# from threading import*
# from time import*

# class MyData:
    
#     def __init__(self):
#         self.data = 0
#         self.flag = False
#         self.lock =Lock()

#     def put(self,d):
#         while self.flag != False:
#             pass
#         self.lock.acquire()
#         self.data = d
#         self.flag = True
#         sleep(1)
#         self.lock.release()
        
#     def get(self):
#         while self.flag != True:
#             pass    

#         self.lock.acquire()
#         x = self.data
#         self.flag = False
#         sleep(1)
#         self.lock.release()
#         return x
    
# def producer(data):
#     i = 1
#     while True:
#         data.put(i)
#         print('producer: ',i)
#         i += 1
        

# def consumer(data):
#     while True:
#         x = data.get()
#         print('consumer: ',x) 
#         #return x

# data = MyData()
# t1 = Thread (target=lambda:producer(data))
# t2 = Thread (target=lambda:consumer(data))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

    


        
# ###  IPC USING CONDITIONS:                              (    NOTIFY , WAIT   )

# from threading import*
# from time import*

# class MyData:

#     def __init__(self):
#         self.data = 0
#         self.cv = Condition()

#     def put(self,d):
#         self.cv.acquire()
#         self.cv.wait(timeout=0)
#         self.data = d
#         self.cv.notify()
#         sleep(1)
#         self.cv.release()
        

#     def get(self):
#         self.cv.acquire()
#         self.cv.wait(timeout=0)
#         x = self.data
#         self.cv.notify()
#         sleep(1)
#         self.cv.release()
#         return x

# def producer(data):
    
#     i = 1
#     while True:
#         data.put(i)
#         print('producer ',i)
#         i += 1

# def consumer(data):
#     while True:
#         x = data.get()
#         print('consumer ',x)

# data = MyData()

# t1 = Thread(target=lambda:producer(data))
# t2 = Thread(target=lambda:consumer(data))

# t1.start()
# t2.start()

# t1.join()
# t2.join()






###  IPC USING QUEUE :                


# from threading import*
# from time import*
# from queue import*

# q =Queue()

# def producer(que):
#     i= 1
#     while True:
#         que.put(i)
#         sleep(1)
#         print('producer ',i)
#         i += 1

# def consumer(que):
#     while True:
#         d = que.get()    
#         print('consumer ',d)
#         sleep(1)
       

# t = Thread(target=lambda:producer(q)) 
# t1 = Thread(target=lambda:consumer(q))

# t.start()
# t1.start()

# t.join()
# t1.join()







###             (  MULTITHREADING USING A  (FUNCTION / METHOD)   )


# from threading import*
# from time import*

# def multitread():
#     for i in range(65,91):
#         print(chr(i))
#         sleep(1)

# t = Thread(target=multitread,name='alphabets')
# t.start()

# for i in range(65,91):
#     sleep(1)
#     print(i)

# t.join()





# ###           (    MULTITHREADING USING A CLASS    )

# from threading import*

# class alphabets(Thread):
#     def run(self): 
#        for i in range(65,91):
#           print(chr(i))

# d = alphabets()
# d.start()

# for i in range(65,91):
#     print(i)

# d.join()





# ###                        (  MUTEX  )                       ##


# from threading import*
# from time import*

# def display(str1):
#     l.acquire()
#     for x in str1:
#         print(x)
#     l.release()


# l = Lock()
# t1 = Thread(target=display,args=('LEARNING PYTHON ',))
# t2 = Thread(target=display,args=('you are welcome ',))

# t1.start()
# t2.start()

# t1.join()
# t2.join()





# ###        (       SEMAPHORE      )   ###

# from threading import*
# from time import*

# def display(str1):

#     l.acquire()
#     for x in str1:
#         print(x)
#     l.release()

# l = Semaphore(2)
# t1 = Thread(target=display,args=('HELLO WORLD ',))        
# t2 = Thread(target=display,args=('you are welcome ',))
# t3 = Thread(target=display,args=('PYTHON LEARNING ',))

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()




# ###    I P C    ( using lock and flag method  )   ###

# from threading import*
# from time import*

# class mydata:

#     def __init__(self):

#         self.data = 0
#         self.flag = False
#         self.lock = Lock()

#     def put(self,d):
#         while self.flag == True:
#             pass
#         self.lock.acquire() 
#         self.data = d
#         self.flag =True
#         sleep(1)
#         self.lock.release()

#     def get(self):
#         while self.flag == False:
#             pass
#         self.lock.acquire()
#         x = self.data
#         self.flag = False
#         sleep(1)
#         self.lock.release()
#         return x
    
# def producer(data):
#     i = 1
#     while True:
#         data.put(i)
#         print('producer :',i)
#         i += 1

# def consumer(data):
#     while True:
#         x = data.get()
#         print('consumer :',x)

# data1 = mydata()

# t1 = Thread(target=lambda:producer(data1))
# t2 = Thread(target=lambda:consumer(data1))
           
# t1.start()
# t2.start()

# t1.join()
# t2.join()






# ###    IPC using Conditions  ###

# from threading import*
# from time import*

# class mydata:

#     def __init__(self):
#         self.data = 0
#         self.cv =Condition()

#     def put(self,d):
#         self.cv.acquire()
#         self.cv.wait(timeout=0)
#         self.data = d
#         self.cv.notify()
#         sleep(1)
#         self.cv.release()

#     def get(self):
#         self.cv.acquire()
#         self.cv.wait(timeout=0)
#         x = self.data
#         self.cv.notify()
#         sleep(1)
#         self.cv.release()
#         return x  

# def producer(data):
#     i = 1
#     while True: 
#         data.put(i)
#         print('producer :',i)
#         i += 1

# def consumer(data):
#     while True:
#        x = data.get()
#        print('consumer :',x)

# d = mydata()

# t1 = Thread(target=lambda:producer(d))
# t2 = Thread(target=lambda:consumer(d))

# t1.start()
# t2.start()

# t1.join()
# t2.join()





# ###  IPC using QUEUE ### 

# from threading import*
# from time import*
# from queue import*

# q = Queue()
 
# def producer(que):
#     i = 1
#     while True:
#         que.put(i)
#         print('producer :',i)
#         i += 1
#         sleep(1)

# def consumer(que):
#     while True:
#         x = que.get()
#         print('consumer :',x)
#         sleep(1)

# t1 = Thread(target=lambda:producer(q))
# t2 = Thread(target=lambda:consumer(q))
    
# t1.start()
# t2.start()

# t1.join()
# t2.join()





















