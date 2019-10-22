import os, random
import matplotlib.pyplot as plt


class PingChecker:
    def __init__(self):
        self.domain = ""
        self.ping_array = []
        pass

    def ping(self, hostname):
        self.domain = hostname
        os.system("ping -n 25 " + hostname + " > C:\\\\Users\\Luke\\Documents\\ping_test.txt")

    def remove_file(self):
        os.remove("C:\\\\Users\\Luke\\Documents\\ping_test.txt")

    def read_ping(self):
        ping_file = open("C:\\\\Users\\Luke\\Documents\\ping_test.txt", "r+")
        lines = ping_file.readlines()

        #domain name followed by the ping over the test
        for x in lines:
            if "time=" in x:
                self.ping_array.append(x.split("time=")[1].split("ms")[0])

        for x in self.ping_array:
            print(x)

        ping_file.close()

    def make_plot(self):
        x_arr = []
        y_arr = []
        y_ticks = []
        for i in range(30):
            y_ticks.append(i*2)
        count = 0
        for x in range(len(self.ping_array)):
            count += 1
            x_arr.append(count)
            y_arr.append(self.ping_array[x]*random.randint(1, 10))
        plt.scatter(x_arr, y_arr)
        plt.gca().invert_yaxis() #yaxis inverted for some reason
        plt.ylabel('Pings (ms)')
        #plt.yticks(y_ticks)
        plt.xlabel('Entry number')
        plt.xticks(x_arr)
        plt.title('Ping test for ' + self.domain)
        plt.show()


if __name__ == '__main__':
    print('hello')
    checker = PingChecker()
    checker.ping('208.67.222.222')
    checker.read_ping()
    checker.make_plot()




