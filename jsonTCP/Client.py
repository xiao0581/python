from socket import *
import json
serverName="127.0.0.1"
serverPort=12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) 
while True: 
        method = input("method:")
        tal1 = input("tal1:")
        tal2 = input("tal2:")
        request = {"method":method,"tal1":tal1,"tal2":tal2}
        message = json.dumps(request)
        clientSocket.send(message.encode())
        respose=clientSocket.recv(1024).decode()
        respose_jason=json.loads(respose)
        if "result" in respose_jason:
            print("result:",respose_jason["result"])           
        elif "error" in respose_jason:
            print("error:",respose_jason["error"]) 
        closeMessage=input("Type exit to close or press enter to continue:")
        if closeMessage.strip().lower() == "exit":
                break    
clientSocket.close()                         
        
   