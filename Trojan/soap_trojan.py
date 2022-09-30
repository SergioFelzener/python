from http import client
import socket
import time

IP = "192.168.0.204"
PORT = 442

def connect(IP, PORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, PORT))
    except Exception as error:
        print("Error Connect", error)

def listen(client):
    try:
        while True:  # infinit loop
            data = client.recv(1024).decode().strip() #envia em bytes faz decode para string / strip remove a quebra de linha 
            if data == "/exit":
                return
            # print(data)
    except Exception as error:
        print("Listen Error : ", error)
        client.close()
            
if __name__ == "__main__":
    while True:
        try:
            client = connect(IP, PORT)
            if client:
                listen(client)
            else:
                print("Connection Fail, Reconnect ... ")
                time.sleep(1)
        except Exception as error:
            print("ERRO : ", error)
        
        
          
    

