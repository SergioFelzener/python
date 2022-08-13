import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        msg = input("mensagem: ") + "\n"
        client.sendto(msg.encode(),("127.0.0.1", 4433)) # enviando dados em connection UDP
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())
        if data.decode() == "sair\n" or msg == "sair\n":
            break
    client.close()
except Exception as error:
    print("Erro de Conexão")
    print(error)