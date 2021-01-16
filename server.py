import socket
import pickle

s = socket.socket()

host = '46.229.212.108'
port = 54320

s.bind((host, port)) 
s.listen(10)

users = {}
nodes = []

while True: 
	c, addr = s.accept()
	print ('Got connection from', addr) 
	data = c.recv(1024)
	mes = pickle.loads(data)
	if mes[1] == "reg":
		users[mes[0]] = (addr[0], int(mes[2]))
	elif mes[1] == "get":
		try:
			c.send(pickle.dumps(users[mes[0]]))
		except:
			pass
	elif mes == "stun":
		c.send(addr[0].encode())
	elif mes == "reg_node" and addr[0] not in nodes:
		nodes.append(addr[0])
	c.close()
