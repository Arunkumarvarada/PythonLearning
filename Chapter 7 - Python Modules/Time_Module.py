import time

print(time.time())

def numbers(max):
    time1= time.time()
    for i in range(0,max):
        print(i)
    time2=time.time()
    print(str(time2-time1))


#numbers(20000)

print(time.asctime())
tup=(2016,10,15,8,45,12,4,0,0)
print(time.asctime(tup))

print(time.localtime())
t= time.localtime()

year=str(t[0])
day=str(t[2])
month=str(t[1])

print(day+"-"+month+"-"+year)

# Sleep demo

for i in range(0,100):
    print(i)
    time.sleep(1)