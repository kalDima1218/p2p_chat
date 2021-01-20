import socket
import pickle

s = socket.socket()

white_server = ('46.229.212.108', 54320) #My server. You can use it for demo. Paste here your server ip to get MUCH SECURE

s.bind(white_server) 
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
	elif mes == "get_nodes":
		c.send(pickle.dumps(nodes))
	c.close()
