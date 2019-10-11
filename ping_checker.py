import os, time
import subprocess

class PingChecker:
    def __init__(self):
        pass

    def ping(self, hostname):
        #for x in range(10):
        pings = os.system("ping -n 25 " + hostname + " > C:\\\\Users\\Luke\\Documents\\ping_test.txt")
        print('this is a test' )
        #print(os.system("ping -n 10 " + hostname))
        #strip out the time variable from

    def remove_file(self):
        os.remove("C:\\\\Users\\Luke\\Documents\\ping_test.txt")

    def read_ping(self):
        ping_file = open(r"C:\Users\Luke\Documents\ping_test.txt","r")
        lines = ping_file.readlines()
        values = []
        # if "time=" in x:
        # print(x["time=":])
        for x in lines:
            print(x)

       # return ping_file


if __name__ == '__main__':
    print('hello')
    checker = PingChecker()
   # checker.ping('google.com')
    checker.read_ping()

    #time.sleep(10)
    #checker.remove_file()


