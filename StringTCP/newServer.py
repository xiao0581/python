from socket import*
import threading
import random
ip=""
serverPort=12000
Server=socket(AF_INET,SOCK_STREAM)
Server.bind((ip,serverPort))
Server.listen(5)
print("Server ready for recive info")
def handle(connectionSocket,addr):
       try:   
              while True:
                     sentence = connectionSocket.recv(1024).decode()
                     if sentence.strip().lower()=="random":
                            connectionSocket.send("input numbers:\n".encode())
                            sentence = connectionSocket.recv(1024).decode()
                            start,end=map(int,sentence.split())
                            randomNumber =random.randint(start,end)
                            connectionSocket.send(str(randomNumber).encode())
                     elif sentence.strip().lower()=="add":
                            connectionSocket.send("input numbers:\n".encode())
                            sentence = connectionSocket.recv(1024).decode()
                            tal1,tal2=map(int,sentence.split())
                            sum =tal1+tal2
                            connectionSocket.send(str(sum).encode())
                     elif sentence.strip().lower()=="subtract":
                            connectionSocket.send("input numbers:\n".encode())
                            sentence = connectionSocket.recv(1024).decode()
                            tal1,tal2=map(int,sentence.split())
                            result =tal1-tal2
                            connectionSocket.send(str(result).encode())
       except Exception as e:
              print(" Client disconnect or exception occurred ", str(e))
       finally:
              connectionSocket.close()
while True:
    connectionSocket, addr = Server.accept()
    threading.Thread(target = handle,args = (connectionSocket,addr)).start()
  