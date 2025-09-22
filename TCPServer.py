from socket import *
import threading
import json

#Husk at sørge for at vi skal læse dictionary 1 linje af gangen

serverPort = 7
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
passwords = []
print ('The server is ready to receive')

def handleClient(connectionSocket, address):
   sentence = connectionSocket.recv(1024).decode()
   passwords.append(sentence)
   print(passwords)
   connectionSocket.close()



while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target = handleClient,args = (connectionSocket,addr)).start()