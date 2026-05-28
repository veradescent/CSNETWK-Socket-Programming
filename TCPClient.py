from socket import *

serverName = 'servername'
serverPort = 5001

num = input('Enter an integer number between 1 and 100:') # accept an integer between 1 and 100
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort)) # connect to server

message = "Hi! I'm Kharlene Monloy " + "num"
clientSocket.send(message.encode())
modifiedMsg = clientSocket.recv(1024)
# wait for server reply
# read server reply
clientSocket.close()
