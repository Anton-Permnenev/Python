__author__ = 'ASUS'
import os
import threading


#pinging and checking response
def ping(hostname):
    response = os.system(' '.join(["ping", hostname]))
    if response == 0:
        #output in file
        f = open('ping results.txt', 'a+')
        f.write(hostname+'\n')

#input&stuff
while True:
    s = input()
    #if s == 'end': break
    try:
        s = input()
    except EOFError:
        break
    print(s)
    t = threading.Thread(target=ping, args=(s,))
    t.start()