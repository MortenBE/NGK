from socket import *
import sys

print(len(sys.argv))
print(str(sys.argv[1]))

serverName = str(sys.argv[1])

serverPort = 9000
clientSocket = socket(AF_INET, SOCK_STREAM)


clientSocket.connect((serverName, serverPort))

clientSocket.send(str(sys.argv[2]).encode())

f = open (str(sys.argv[2]), 'wb')
while True:


    data = clientSocket.recv(1000)

    while(data):
        print("Recieving data")
        f.write(data)
        data = clientSocket.recv(1000)
        print("Bytes recieved", len(data))
    f.close()

    clientSocket.close()
