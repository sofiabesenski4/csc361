import sys
from socket import *
import random
import time
print "initiating a client application which will send a request, and recieve packets"

CLIENT_PORT=random.randrange(8000,12000)

SERVER_HOSTNAME= sys.argv[1]
SERVER_PORT=sys.argv[2]
filename_requested = sys.argv[3]



print "server ip {} serverport {}".format( SERVER_HOSTNAME, SERVER_PORT)


client_socket = socket(AF_INET, SOCK_STREAM)

client_ip= gethostbyname(gethostname())

client_socket.bind((client_ip,int(CLIENT_PORT)))

client_socket.connect((SERVER_HOSTNAME,int(SERVER_PORT)))

try:
    message = "GET {} HTTP/1.1\nHost:{}\n\n".format(filename_requested,SERVER_HOSTNAME)
    print >>sys.stderr, 'sending "%s"' % message
    client_socket.sendall(message)
    recieved_string=""
    while 1:
        response = client_socket.recv(16)
        recieved_string=recieved_string + response
        time.sleep(0.02)
        if not response:
			break
    print recieved_string

finally:
	print "finished recieving"
	client_socket.close()
	
