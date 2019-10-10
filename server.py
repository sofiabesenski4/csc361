#import socket module
from socket import *
import sys # In order to terminate the program

server_socket = socket(AF_INET, SOCK_STREAM)


#Prepare a server socket
print "Server starting: Python version : ", sys.version

#specifying a port to bind the webserver to, arbitrary non-privileged port
PORT=11112

#finding the IP adr of the machine the server is running on
host_name= gethostbyname(gethostname())
print "host_name=",host_name, "on port: ", PORT

server_socket.bind((host_name,PORT))
server_socket.listen(5)
while True:
    #Establish the connection
    
    
    print('Ready to serve...')
    #connectionSocket, addr =  ??????????????? 
    connection_socket, addr = server_socket.accept()
    print "Server connected by ", addr
    
    
    # now trying to read from the file specified
    try:
        message = connection_socket.recv(1024);
        print "total message received from client", message
        filename = message.split()[1]                
        f = open(filename)
        
        output_data = f.read()
        #Send one HTTP header line into socket
        connection_socket.send("HTTP/1.1 200 OK\n\n".encode())
        print "output data: {}\n".format(output_data)
        #Send the content of the requested file to the client
        
        for i in range(0, len(output_data)):
			print "character{}: {}".format(str(i),output_data[i].encode())           
			connection_socket.send(output_data[i].encode())
        connection_socket.send("\n\n".encode())
        
        connection_socket.close()
    except IOError:
		print("IOERROR: file %s not found" %filename)
		connection_socket.send("HTTP/1.1 404 Not Found\r\n\n".encode())
        #Send response message for file not found
        #????????????
		connection_socket.send("The requested file was not found\r\n\n".encode())
		#Close client socket
        #????????????
		connection_socket.close()
server_socket.close()
sys.exit()#Terminate the program after sending the corresponding data
