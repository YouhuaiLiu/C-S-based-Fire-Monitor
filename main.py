from tcp import *
from time import *
from gpio import *

port = 1234
server = TCPServer()

def onTCPNewClient(client):
	def onTCPConnectionChange(type):
		print("connection to " + client.remoteIP() + " changed to state " + str(type))
		
	def onTCPReceive(data):
		print("received from " + client.remoteIP() + " with data: " + data)
		# send back same data
		if data == "Fire":
			customWrite(0,1)
			customWrite(4,1)
		else:
			customWrite(0,0)
			customWrite(4,0)
		client.send(data)

	client.onConnectionChange(onTCPConnectionChange)
	client.onReceive(onTCPReceive)

def main():
	server.onNewClient(onTCPNewClient)
	print(server.listen(port))

	# don't let it finish
	while True:
		sleep(3600)

if __name__ == "__main__":
	main()
