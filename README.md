Project FlowerMonkey
Developer: Ruben Thijssen (@rubenthijssen) http://www.damnsecure.org 
Copyright (c) 2012 DamnSecure

Project FlowerMonkey is a (simple) tool that allows you to discover and/or extract data from a directory that contains a .svn directory.
See http://www.damnsecure.org/<blog-post> for more details

USAGE:
To run this tool you only need to provide a url (example: http://www.damnsecure.org). The tool will then visit the .svn directory of the provided url. In the case of the example url this would be 'http://www.damnsecure.org/.svn'. From there on the wcprops-all file will be downloaded and all the paths will be extracted. Then based on the regex defined in 'run.py' the files matching the regex will be downloaded. If needed change the regex (or the rest of the script) to your needs.

DISCLAIMER:
This is only for testing and educational purposes and can only be used where strict consent has been given. Do not use
this for illegal purposes and use responsibly. When unsure what this tool does read the given blogpost and/or the source code, or contact the developer(s).

LICENSE:
Code is completely free. Would be nice if you contributed though, instead of keeping it to yourself ;) Sharing is knowing.
