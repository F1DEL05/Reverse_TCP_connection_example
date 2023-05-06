#LISTENER  wILL wORK IN OUR DEVICE

import socket

#PORT IS CHANGEABLE

address=("YOUT IP", 2005)

main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#LISTENING 2005 PORT
main_socket.bind(address)
main_socket.listen()

print(f"{address[0]}:{address[1]} is Listening by us")

# .ACCEPT() FUNCTION IS RETURNING TARGET SOCKET AND IP ADDRESS VALUES
target_socket, target_address= main_socket.accept()

print("\n\n{}:{} Connected to server !\n\n".format(target_address[0],target_address[1]))
a=0
while True:
	a+=1
	if a==1:
		print("Hi !")
