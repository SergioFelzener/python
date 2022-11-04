import requests
import time
from bs4 import BeautifulSoup

with open("server_list.txt", "r") as file:
    server_list = file.read().splitlines()
    
    for server in server_list:
        try:
            response = requests.get(server, timeout=2)
            content = response.content
            status = response.status_code
            # print(status)
            site = BeautifulSoup(content, 'html.parser')
            login_rec = site.find('div', attrs={'class': 'login-content'})
            if login_rec != "":
                print("Server => {} *** Status code-> {} ***".format(server, status))
            else:
                print("Server => {} *** Status code-> {} ***".format(server, status))
        except Exception as error:
            print("SERVER IS DOWN ->  {}".format(server))
            pass

# print("Status code => {} ".format(response.status_code))
# print(" Header ")
# print(response.headers)
# print("\n\n")
# print(" Content ")
# print(response.content)
# print(type(response.content))

# content = response.content

# site = BeautifulSoup(content, 'html.parser')

# print(" Site ")

# # print(site.prettify())

# login_rec = site.find('div', attrs={'class': 'login-content'})

# print(login_rec)




