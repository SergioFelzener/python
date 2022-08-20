import socket 
import sys

host = "google.com"
# port = 77


def scan(host, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)

            code = client.connect_ex((host, int(port)))

            if code == 0:
                print("[+] {} open".format(port))
            else:
                print("[-] {} Port Closed :(".format(port))
    except Exception as error:
        print("Error : " + error)
            

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            ports = sys.argv[2].split(",")
            if len(sys.argv) >= 4:
                timeout = sys.argv[3]
        else:
            ports = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135, 800, 1000, 1001, 1101, 1011]
        
        scan(host, ports)
            
    else:
        print ("Error: To use portscan (portscan.py host, ports) type:\nphyton3 portscan.py host.com, 22,33,1000")
