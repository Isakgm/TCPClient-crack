from socket import *
import json

# slags konstanter
serverName = 'localhost'
serverPort = 7


clientSocket = socket(AF_INET, SOCK_STREAM) # Stream = tcp
clientSocket.connect( (serverName,serverPort) )

sentence = sentence + '\r\n' # '\r\n' er for at lave et linjeskift så det også virker med en c# server
byteSentence = sentence.encode() # laver tegn til byte
clientSocket.send(byteSentence)

#venter på svar
returnSentence = clientSocket.recv(1024)
jsonL = json.loads(returnSentence.decode())
print('Modtaget: ', jsonL) # byte til tegn

clientSocket.close()