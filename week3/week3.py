import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # internet socket, stream socket
mysock.connect(("www.data.pr4e.org", 80))

mysock.send('GET http://www.data.pr4e.org/intro-short.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if len(data)<1 :
        break
    print data
mysock.close()
# import urllib
# fhand = urllib.urlopen('http://www.data.pr4e.org/intro-short.txt')
#
# for line in fhand:
#     print line
