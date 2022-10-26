from scapy.all import *

# pacote = IP(version=70, dst="192.168.0.179", src="0.0.0.0")/ "ENVIO DE DADOS NO PACOTE"   pacote IP 
# pacote = ARP()  pacote arp
# pacote = TCP(dport=22, flags="A")/"data:HELLO" # pacote TCP 
# pacote = IP()/TCP() # tcp ip 
# pacote = Ether()/IP()/TCP(dport=22, flags="A")/"data : data do pacote (conteudo)" # usando baixo nível com Ethernet0.
# pacote.show()

# enviando pacote
# pacote = IP(dst="google.com")
# pacote.show()
# send(pacote)

## PING 
# verificando pacotye ICMP

# pacote = ICMP()
# pacote.show()

#pingando
# pacote = IP(dst="google.com")/ICMP()
# pacote.show()
# send(pacote)

# criando ataque ne negaçao de serviço
# pacote = IP(dst="google.com")/ICMP()
# pacote.show()
# send(pacote, loop=1)

## recebendo resposta 

# pacote = IP(dst="google.com")/ICMP()
# # pacote.show()
# respondidos, nao_respondidos = sr(pacote)
# print(respondidos)


# pacote = IP(dst="google.com")/ICMP()
# # pacote.show()
# respondidos, nao_respondidos = sr(pacote)
# print(nao_respondidos)

# Ping SCAN verificar quais hosts estão ativos dentro de uma rede 

# pacote = IP(dst="192.168.0.0/30")/ICMP()
# # pacote.show()
# respondidos, nao_respondidos = sr(pacote, timeout=0.2)
# for n in range(len(respondidos)):
#     print(respondidos[n][0][IP].dst)
    
# print(respondidos) ## remover

# PORT SCAN

hosts = ["receiv.it", "bancocn.com", "google.com"]

pacote = IP(dst=hosts)/TCP(dport=(1,500)) # passado range de portas
# pacote.show()
respondidos, nao_respondidos = sr(pacote, timeout=1)
for n in range(len(respondidos)):
    print("{} -> {}".format(respondidos[n][0][IP].dst, respondidos[n][0][TCP].dport))  ## ABRIR NC LOCAL para teste



