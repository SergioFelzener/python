import socket

url = "google.com"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 2 arguments (familia , tipo) TCP 
client.settimeout(5) #esperando connection em 1 segundo - caso nao seja estabelecida feche a connection
#print(client)
try:
    client.connect((url, port))
    client.send(b"GET / HTTP/2\nHost: www.google.com\n\n\n")# teste no goolge - rpecisa usar 3x \n para saber que é uma requisição http
    # client.send(b"GET /html/new/login HTTP/2\nHost: qa-01.receiv.it\n\n\n")
    reciv_packs = client.recv(1024).decode() # necessário decode para decodificar os bytes em string (neste caso)
    print(reciv_packs)
except:
    print ("Erro de Conexao, Recusada !")

