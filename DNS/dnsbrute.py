import dns.resolver
import sys

resolver = dns.resolver.Resolver()

try:
    target = sys.argv[1]
    wordlist = sys.argv[2]

except:
    print("Error: Missing Arguments use syntax:\ndnsbrute.py target.com wordlist.txt")
    sys.exit()
    

# target = "bancocn.com"

#wordlist = ["teste", "advanced", "shop", "admin", "panel", "mysql", "ftp", "smtp", "control", "api"]
try:
    with open(wordlist, "r") as file:    # Use crunch to generate your wordlist file =/
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
        pass
        # print("Subdomain does not exist")
        # print(error)
        



