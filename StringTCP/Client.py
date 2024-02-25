from socket import *
serverName="127.0.0.1"
serverPort=12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) 
while True: 
        message = input("")
        clientSocket.send(message.encode())
        if message.strip().lower() == "close":
                break
        modifiedMessage = clientSocket.recv(1024)
        print("Received from server:", modifiedMessage.decode())
clientSocket.close()      