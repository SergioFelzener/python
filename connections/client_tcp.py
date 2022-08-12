import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 2 arguments (familia , tipo) TCP 
client.settimeout(1) #esperando connection em 1 segundo - caso nao seja estabelecida feche a connection
#print(client)
try:
    client.connect(("127.0.0.1", 4000))
    #client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n") # teste no goolge - rpecisa usar 3x \n para saber que é uma requisição http
    client.send(b"send message to client connection ---- Hello ----\n") # teste no goolge ("b" -> antes converte string para bytes)
    reciv_packs = client.recv(1024).decode() # necessário decode para decodificar os bytes em string (neste caso)
    print(reciv_packs)
except:
    print ("Erro de Conexao, Recusado !")

# teste criando uma conexão local NetCat
# nc -lvp 4000 



