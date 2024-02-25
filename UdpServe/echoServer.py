from socket import *
servicePort=8989
socketServer=socket(AF_INET,SOCK_DGRAM)
socketServer.bind(("127.0.0.1",servicePort))
print("The server is ready to receive")

while True:
      message,cilentAdrr=socketServer.recvfrom(2048)
      modifiedMessage =message.decode().upper()
      socketServer.send(modifiedMessage.encode(),cilentAdrr)
