#Client python code
from socket import *
import sys

print(len(sys.argv))
print(str(sys.argv[1]))

#The socket module forms the basis of all network communications in Python. By including this line, we
#will be able to create sockets within our program.
serverName = str(sys.argv[1])
#The first line sets the variable serverName to the string ‘hostname’. Here, we provide a string
#containing either the IP address of the server (e.g., “128.138.32.126”) or the hostname of the server
#(e.g., “cis.poly.edu”). If we use the hostname, then a DNS lookup will automatically be performed to get
#the IP address.) The second line sets the integer variable serverPort to 12000.
serverPort = 9000
clientSocket = socket(AF_INET, SOCK_STREAM)
#AF_INET is the client socketself.
#SOCK_STREAM indicates that it is an TCP Connection

clientSocket.connect((serverName, serverPort))

#sentence = input("Enter filename: ")
#writeTextTCP(sentence, serverPort)
clientSocket.send(str(sys.argv[2]).encode())

f = open (str(sys.argv[2]), 'wb')
while True:


    data = clientSocket.recv(1000)
    #print("data:", (data))

    while(data):
        print("Recieving data")
        f.write(data)
        data = clientSocket.recv(1000)
        print("Bytes recieved", len(data))
    f.close()

    clientSocket.close()






#modifiedSentence = clientSocket.recv(1024)
#print("From Server: ", modifiedSentence.decode())
#clientSocket.close()
