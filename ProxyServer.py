from socket import *
import sys

if len(sys.argv) <= 1:
 	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
 	sys.exit(2)
 	
# The proxy server is listening at 8888 
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((sys.argv[1], 8888))
tcpSerSock.listen(100)

count = 0
while 1:
 	# Strat receiving data from the client
    print('Ready to serve...')
 	## FILL IN HERE...
    count = count+ 1
    print(count)
    #this snippet of code is from Computer Networking book
    connectionSocket, addr = tcpSerSock.accept()

        
    sentence = connectionSocket.recv(1024).decode()
    # connectionSocket.send(capitalizedSentence.encode())       #will be used later below
    
    
    print('Received a connection from:', addr)
    
    message = sentence ## FILL IN HERE...
    print(message)
    
    
 	# Extract the filename from the given message
    servername = message.split("/")[1].split()[0]
    serverName = "www." + servername
    print(serverName)


 	## FILL IN HERE...
    serverPort = 80
    tcpCliSock =  socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect((serverName, serverPort))
    

    
    # print(tcpCliSock.getsockname()) #used to test that the connection was made

    tempFile = tcpCliSock.makefile('rw', 1)
    # print(tempFile)               #used to debug and make sure the right mode was selected
    tempFile.write("GET " + "http://" + serverName + " HTTP/1.0\n\n")

    
    filetouse = tempFile.read()## FILL IN HERE...

    # print(filetouse)          #used for debugging bbc.com
    connectionSocket.send(filetouse.encode())
    modifiedfiletouse = tcpCliSock.recv(1024)
    

    fileExist = False
    
    try:
		# Check wether the file exist in the cache

		## FILL IN HERE...
        f = open(servername + ".txt", "r")
        urllist= f.readlines()
        fileExist = True
		# ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")            
        tcpCliSock.send("Content-Type:text/html\r\n")


		## FILL IN HERE...

        print("It's from the cache")

#  	#Error handling for file not found in cache, need to talk to origin server and get the file
    except IOError:
        if fileExist == False: 

 			# FILL IN HERE...
             print(1234)
             # except:
             #     print("Illegal request")                                               
        else:
 			# HTTP response message for file not found
             Sock.send("HTTP/1.0 404 sendErrorErrorError\r\n")                             
             Sock.send("Content-Type:text/html\r\n")
             CliSock.send("\r\n")

 	#Close the client and the server sockets   

        tcpCliSock.close() 
tcpSerSock.close()