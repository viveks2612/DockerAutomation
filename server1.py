import socket
import os


s = socket.socket()
ip="192.168.43.45"
port=1114
s.bind( (ip,port) )
s.listen()

client_session , client_address = s.accept()


while True:
	data = client_session.recv(20)
	choise = data.decode()
	if int(choise)==1:
		os.system("file")
	elif int(choise)==2:
		os.system("filegit")
	
