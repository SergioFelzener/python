import requests

# request = requests.get("http://shop.bancocn.com/rest/products/1/reviews")
# data_json = request.json()
# print(data_json)

for i in range(36):
    response = requests.get("http://shop.bancocn.com/rest/products/{}/reviews".format(i))
    print(response.text)