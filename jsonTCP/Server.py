from socket import*
import json
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
                     request= json.loads(sentence)
                     method = request.get("method")
                     tal1 = request.get("tal1")
                     tal2 = request.get("tal2")
                     if method=="random":
                            result = random.randint(int(tal1),int(tal2))  
                            response = {"result":result}   
                            connectionSocket.send(json.dumps(response).encode())                                                    
                     elif method=="add":
                            result = int(tal1)+int(tal2)
                            response={"result":result}
                            connectionSocket.send(json.dumps(response).encode())
                     elif method=="subtract":
                            result = int(tal1)-int(tal2)
                            response={"result":result}
                            connectionSocket.send(json.dumps(response).encode())
                     else:
                            response={"error":"method not found"}
                            connectionSocket.send(json.dumps(response).encode())       
       except json.JSONDecodeError as e:
              print(" Invalid Json format ", str(e))
       except Exception as e:
              print(" Client disconnect or exception occurred ", str(e))
       finally:
              connectionSocket.close()
while True:
    connectionSocket, addr = Server.accept()
    threading.Thread(target = handle,args = (connectionSocket,addr)).start()
  