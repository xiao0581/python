from socket import*
serverName="127.0.0.1"
ServerPort=8989
clientScoket=socket(AF_INET,SOCK_DGRAM)
message=input("input lowercase sentence:")
clientScoket.sendto(message.encode(),(serverName,ServerPort))
modifiedMessage, serverAddress = clientScoket.recvfrom(2048)
print(modifiedMessage.decode())
clientScoket.close()