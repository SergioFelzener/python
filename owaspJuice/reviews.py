import requests

EMAILS = []

for i in range(36):
    response = requests.get("http://10.10.110.200/rest/products/{}/reviews".format(i))
    data_json = response.json()
    for review in data_json["data"]:
        email = review["author"]
        if email not in EMAILS:
            print(review["author"])
            EMAILS.append(email)