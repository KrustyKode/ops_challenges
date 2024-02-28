#!/usr/bin/env python3

import requests
import webbrowser
import os

# Assuming the target site supports cookies and the session.
targetsite = "http://www.whatarecookies.com/cookietest.asp"
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster():
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
    ''')

# Send cookie back to the site and receive a HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)

# Generate a .html file to capture the contents of the HTTP response
filename = '/tmp/response.html'
with open(filename, 'w') as file:
    file.write(response_with_cookie.text)

bringforthcookiemonster()
print("Target site is " + targetsite)
print("Cookie returned to the site, response captured in " + filename)

# Open it with Firefox (using webbrowser module)
webbrowser.open_new_tab('file://' + filename)

