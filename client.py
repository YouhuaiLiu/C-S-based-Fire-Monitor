from tcp import *
from time import *
from gpio import *

serverIP = "192.168.16.4"
serverPort = 1234

client = TCPClient()

def onTCPConnectionChange(type):
	print("connection to " + client.remoteIP() + " changed to state " + str(type))

def onTCPReceive(data):
	print("received from " + client.remoteIP() + " with data: " + data)

def main():
	client.onConnectionChange(onTCPConnectionChange)
	client.onReceive(onTCPReceive)

	print(client.connect(serverIP, serverPort))

	count = 0
	while True:
		if digitalRead(0) != 0:
			data1 = "Fire"
			client.send(data1)
		elif digitalRead(0) == 0:
			data1 = "nothing"
			client.send(data1)
	
		sleep(5)

if __name__ == "__main__":
	main()
