import socket, time
from PIL import Image, ImageOps
from pyzbar import pyzbar



ip = "172.18.4.3"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
print(s.recv(1024).decode())
s.send(b"Ok")

while 1:

    time.sleep(0.5)
    data = s.recv(1000000).decode()
    print(data)
    data = data.replace(" ", "").split(";") 

    qrcode = Image.new("RGB", (len(data), len(data)))
    data.pop(-1)
    for i in range(len(data)):
        data[i] = data[i].split("),(")
        for j in range(len(data)):
            data[i][j] = tuple(map(int, data[i][j].replace("(", "").replace(")", "").split(",")))
            pixel = data[i][j]
            # print(pixel)
            # print((i,j), pixel)
            qrcode.putpixel((i,j), pixel)
                
            
    qrcode = ImageOps.expand(qrcode, border=3, fill="white")
    # qrcode.save("qrcode3.png")
    # print(pyzbar.decode(qrcode)[0][0])
    s.send(pyzbar.decode(qrcode)[0][0])
    print(s.recv(1000000))

    # print(len(data))

