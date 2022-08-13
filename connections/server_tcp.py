import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(('0.0.0.0', 8883)) # porta que aguarda o clinet se conectar 0.0.0.0 -> dinamico consigo conectar de qq ip
    server.listen(5)
    print("Connection OK ...")
    print("Listening........")
    
    client_socket, address = server.accept()
    client_socket.send(b"Conected success...\nSend Message :")
    
    while True:
        print("Connection from ip :" + address[0] + "\nWaiting...")
        data = client_socket.recv(1024).decode()
        if data == "senhasecreta\n":
            print(data + "\n")
            client_socket.send(b"Mensagem Secreta DONE !!!!\n")
        else:
            print("response :" + data + "\n")
            client_socket.send(input("Mensagem: ").encode())
    server.settimeout(30)
    server.close()
except Exception as error:
    print("Erro: ", error)
    server.close()