import paramiko # biblioteca ssh para facilitar a construção melhor que usar socket

host = "127.0.0.1"
user = "kali"
passwd = "kali"

client = paramiko.SSHClient() # criando objeto client
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # setando host como conhecido 
client.connect(host, username=user, password=passwd) #conectando

# print(client.exec_command("ls")) # executando comando no ssh conectado # verificando retorno tupla com 3 objetos
while True:
    stdin, stdout, stderr = client.exec_command(input("Command: "))
    for line in stdout.readlines():
        print(line.strip())
    
    error = stderr.readline()
    if error:
        print("erro: " + error)
    





