import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt'.encode()
s.send(cmd)

while True:
	data = s.recv(512)
	if (len(data) < 1):
		break
	print(data.decode())
s.close()
