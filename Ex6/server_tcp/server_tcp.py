from socket import *
serverPort = 9000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Got connection from", addr)
    sentence = connectionSocket.recv(1000).decode()
    print("Server recived: ", sentence)

    f = open(sentence,'rb')
    l = f.read(1000)
    print(len(l))

    while (l):
        print("Sending, bytes:",len(l))
        connectionSocket.send(l)
        l = f.read(1000)

    f.close()
    print("Done")
connectionSocket.close()


#connectionSocket.send(capitalizedSentence.encode())
