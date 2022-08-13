import socket  
# Criando servidor para escutar em uma porta e receber conexão tcp pelo NetCat

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# file = open("output.txt", "w")
try:
    server.bind(('0.0.0.0', 7773)) # porta que aguarda o clinet se conectar 0.0.0.0 -> dinamico consigo conectar de qq ip
    server.listen(5) #usando metodo para poder escutar - parametro - numero de conexoes
    print("Connection OK ...")
    print("Listening........")
    # atribuindo tupla em duas variáveis 
    client_socket, address = server.accept() #retorna tupla 1 elemento socket / segundo elemento outra tupla com ip e porta
    client_socket.send(b"Conected success...\nSend Message :")
    
    
    # chat
    while True:
        print("Connection from ip :" + address[0] + "\nWaiting...")
        data = client_socket.recv(1024).decode()
        if data == "senhasecreta\n":
            print(data + "\n")
            # print("passou aqui \n")
            client_socket.send(b"Accept Code DONE.\nConnection CLOSE!")
            print(server.close()) # Nao esta fechando a conexao verificar.
        else:
            print("response :" + data + "\n")
            client_socket.send(input("Mensagem: ").encode())
    server.settimeout(30)
except Exception as error:
    print("|DeBuG|Informação do sistema ->")
    print("Erro: ", error)
    print("dentro da exception")
    server.close()