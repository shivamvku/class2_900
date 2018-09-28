# # import time
# # from threading import Thread

# # c = 5000

# # def count(n):
# # 	while n>0:
# # 		n-=1
# # start = time.time()
# # count(c)
# # end = time.time()

# # print('The Total counsumed time in sec is ',end - start)



# # import time
# # from threading import Thread

# # c = 5000

# # def count(n):
# # 	while n>0:
# # 		n-=1
# # t1 = Thread(target = count,args = (c//2,))
# # t2 = Thread(target = count,args = (c//2,))
# # start = time.time()
# # t1.start()
# # t2.start()

# # t1.join()
# # t2.join()

# # end = time.time()
# # print('The Total counsumed time in sec is ',end - start)


# import os
# import threading
# from threading import Thread

# def f1(a):
# 	print(' The Process ID of {} is {}'.format(threading.current_thread().name,os.getpid()))

# 	print('The Output is ',a**2)

# def f2(a):
# 	print(' The Process ID of {} is {}'.format(threading.current_thread().name,os.getpid()))

# 	print('The Output is ',a**3)


# if __name__ == '__main__':
# 	print(' The Process ID of {} is {}'.format(threading.current_thread().name,os.getpid()))

# 	t1 = threading.Thread(target = f1,args= (2,),name = 'squring')

# 	t2 = threading.Thread(target = f2,args= (2,),name = 'cubing')

# 	t1.start()
# 	t2.start()

# 	t1.join()
# 	t2.join()

# 	