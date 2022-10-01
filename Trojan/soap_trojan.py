from http import client
import socket
import time

IP = "192.168.0.204"
PORT = 443

def connect(IP, PORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, PORT))
        print(client)
    except Exception as error:
        print("Error Connect", error)

# def listen(client):
#     try:
#         while True:  # infinit loop
#             data = client.recv(1024).decode().strip() #envia em bytes faz decode para string / strip remove a quebra de linha 
#             print(data)
#             if data == "/exit":
#                 return
#             # print(data)
#     except Exception as error:
#         print("Listen Error : ", error)
#         client.close()

def listen(client):
    try:
        while True:
            data = client.recv(1024).decode().strip()
            if data == "/exit":
                return
            # else:
            #     threading.Thread(target=cmd, args=(client, data)).start()

    except Exception as error:
        print("Error listen", error)
        client.close()
            
if __name__ == "__main__":
    while True:
        client = connect(IP, PORT)
        if client:
            listen(client)
        else:
            print("Conexao deu erro, tentando novamente")
            time.sleep(3)
        
        
          
    

