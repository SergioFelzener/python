import requests


try:
    server = requests.get("https://qa-07.receiv.it/html/new/login", timeout=5)
    print(server.status_code)
except Exception as error:
    print("ERRO NO SERVER =>", error)
    pass
