from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)

    if message == b'u' or message == b'U':
        print("Recieved ", message)
        f = open('/proc/uptime','rb')
        l = f.read(1000)
        serverSocket.sendto(l, clientAddress)

    elif message == b'l' or message == b'L':
        print("Recieved ", message)
        f = open('/proc/loadavg','rb')
        l = f.read(1000)
        serverSocket.sendto(l, clientAddress)

    else:
        print("Recieved ", message)
        print("No valid message recieved")
        serverSocket.sendto("Error".encode(), clientAddress)
