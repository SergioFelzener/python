from curses import ERR
import socket



try: 
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    s.bind(("eth0", 0)) #// definindo interface
    print(s.recvfrom(64535))
except Exception as error:
    print("Erro >>>>", error)
    
