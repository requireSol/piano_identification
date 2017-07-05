import time
import thread
import recording
print('hi')

def option1():
    print("""[1] RECORDING [1]""")
    record_time = int(raw_input('ENTER RECORDING TIME (IN SECONDS): '))
    for i in range(5)[::-1]:
        print("RECORDING IS ABOUT TO START...%d" % (i + 1))
        time.sleep(1)
    print("RECORDING HAS STARTED - IT WILL AUTOMATICALLY STOP IN %d SECONDS" % record_time + 4)


print("""
0: help
1: record images
2: create abc-notation from images
""")
c = raw_input()

if c == '0':
    print("""infomartion ----""")
elif c == '1':
    option1()

elif c == '2':
    print("""enter the path of the images""")

else:
    print("""unknown option""")



