#!/usr/bin/python

import http, json

def printConnInfo():
    connection = json.loads(http.getUrl('http://ifconfig.me/all.json').read())
    print "[*] Your current connection info is: "
    print "     IP: %s" % connection["ip_addr"]
    print "     User-Agent: %s" % connection["user_agent"]

# Check if tor is being used
def checkTor():
    print "[*] Checking Tor connection..."

    page = http.getUrl(url="http://check.torproject.org/").read()
    if page and 'Congratulations' in page:
        print "[*] Tor is (still) your friend"
        return True
    elif page and 'Sorry' in page:
        print "[*] I was able to connect via HTTP but Tor doesn't seem to be working"
        return False
    else:
        print "[*] Something went wrong (don't really care what). Quiting..."
        return False
