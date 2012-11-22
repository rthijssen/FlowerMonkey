#!/usr/bin/python

# START - this code is needed to prevent DNS leaks
import socks
import socket

def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

# END - DNS leak prevention

# HTTP Module code
import urllib2

tor = False
user_agent = "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1"

# Set our current proxy
def setProxy(type=socks.PROXY_TYPE_SOCKS5, host="127.0.0.1", port="9050"):
    socks.setdefaultproxy(type, host, port)
    socket.socket = socks.socksocket
    socks.wrapmodule(urllib2)

def getUrl(url):
    # We need to set the proxy defaults before a socket is created to make sure all traffic is going through our proxy
    if tor: setProxy(type=socks.PROXY_TYPE_SOCKS5, host='127.0.0.1', port=9050)
    
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request) 

    return response
