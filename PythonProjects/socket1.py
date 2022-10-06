import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('zty.pe', 443))
cmd = 'GET https://zty.pe'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(1024)
	if (len(data) < 1):
		break
	print(data.decode())
mysock.close()
