import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 2 arguments (familia , tipo) TCP 
#print(client)
client.connect(("google.com", 80))
client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n")
reciv_packs = client.recv(10024).decode()
print(reciv_packs)


