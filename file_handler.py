#/!/usr/bin/python

def writeDataToFile(filename, data, quitOnFail=False):
    f = file("output/"+filename, "a")
    f.write(data)
    f.flush()
    f.close()
    print "[*] Successfully saved %s" % filename
