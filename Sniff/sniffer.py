import socket
import struct 
## try run Python as ROOT (by S0@pX3B0x)

# try: 
#     s.bind(("eth0", 0)) #// definindo interface
#     # print(s.recvfrom(64535))
#     data, source = s.recvfrom(64535)
# except Exception as error:
#     print("Erro >>>>", error)


def ethernet_frame(data):    
    dst_mac, src_mac, ethernet_type = struct.unpack("! 6s 6s H", data[:14])# passar formato que irá converter expl : char de x bytes ou int de x bytes segundo argumento dados de unpac para manipular no python
    return dst_mac, src_mac, ethernet_type, data[14:]
    #print(dst_mac, src_mac, ethernet_frame_type)
    
if __name__ == "__main__":
    data = []
    source = []
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while 1:
        data, source, s.recvfrom(65535)
        print(ethernet_frame(data))
    


 