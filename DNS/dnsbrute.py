import dns.resolver
import sys

resolver = dns.resolver.Resolver()

# try:
#     target

# except:
    

target = "bancocn.com"

#wordlist = ["teste", "advanced", "shop", "admin", "panel", "mysql", "ftp", "smtp", "control", "api"]
try:
    with open("wordlist.txt", "r") as file:    # Use crunch to generate your wordlist file =/
        subdomains = file.read().splitlines()
except Exception as error:
    print("File not found")
    print(error)
    sys.exit()

for subdomain in subdomains:

    try:
        sub_target = "{}.{}".format(subdomain, target)
        results = resolver.resolve(sub_target, "A") # host e classe de IP A = ipv4 (AAAA = iPv6)
        for result in results:
            print("{} -> {}".format(sub_target, result))
    except Exception as error:
        print("Subdomain does not exist")
        print(error)
        



