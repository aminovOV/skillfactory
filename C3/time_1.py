import time
# import time as t
# # # print(time.time()) sec from start of epoch
# # x = time.time()
# # a = time.gmtime(x)  # UTC
# # zz = time.ctime()
# # print(type(zz))  # local time
# # print(time.localtime()[0])
# # x = time.localtime()
# x = time.strftime("%A, %d %b %Y %H:%M:%S +0000", time.gmtime())
# print(x)

timer = 10
for i in range(0, timer+1):
    print(timer)
    timer -= 1
    time.sleep(1)
print('Время вышло')
