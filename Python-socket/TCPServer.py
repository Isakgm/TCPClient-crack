from socket import *
import threading
import json

results = []

def read_in_chunks(filename = "webster-dictionary.txt", chunk_size=5000):
    chunks = []
    with open(filename, "r", encoding="utf-8") as f:
        chunk = []
        for i, line in enumerate(f, start=1):
            chunk.append(line.strip())  # strip newline
            if i % chunk_size == 0:
                chunks.append(chunk)
                chunk = []
        # Add the last chunk if it has leftover lines
        if chunk:
            chunks.append(chunk)
    return chunks

i = 0
serverPort = 7
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

async def handleClient(connectionSocket, address):
   sentence = connectionSocket.recv(1024).decode()
   print(sentence)
   
   
   chunkToSend = json.dumps(chunks[i])

   connectionSocket.send(chunkToSend.encode())
   await i=i+1

   if len(sentence) > 0:
       results.add(json.loads(sentence))
   


#def splitIntoChunkz():

while True:
    read_in_chunks()
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target = handleClient,args = (connectionSocket,addr)).start()