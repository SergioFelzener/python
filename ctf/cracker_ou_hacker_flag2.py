import socket
import re

ip = "172.18.1.3"
port = 50123

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
data = s.recv(1024)
sum = 0
numberlist = re.split("\D+", data)
numberlist = ' '.join(numberlist).split()
print(numberlist)

for number in numberlist:
    sum+=int(number)

s.send(str(sum))
print(s.recv(1024))


# print(numberlist)


