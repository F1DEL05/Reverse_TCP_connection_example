#CLIENT wILL wORK IN TARGET COMPUTER FOR SENDING CONNECTION REQUEST TO US

import socket

#PORT is changeable

address=("CONNECTION IP",2005)

socket_t=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	socket_t.connect(address)
except:
	print("Connection Failure !")

a=0
while True:
	a+=1
	if a==1:
		print("Connection Succesfull !")
