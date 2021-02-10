import socket 
import threading
import pickle
from aes import encrypting, decrypting
from netifaces import interfaces, ifaddresses, AF_INET

white_server = ('46.229.212.108', 54320) #My server. You can use it for demo. Paste here your server ip to get MUCH SECURE

def receving(key, sock):
	try:
		while 1:
			data, addr = sock.recvfrom(1024)
			print ('New message: '+ decrypting(data, key))
	except:
		pass

def client_connecting(ip, port):
	global white_server
	key = "paymerespect"
	
	s = socket.socket() 
	s.connect(white_server)
	name = input("Enter your name: ")
	s.send(pickle.dumps((name, "reg", str(port))))
	s.close()
	
	s = socket.socket() 
	s.connect(white_server)
	client = input("Enter client name: ")
	s.send(pickle.dumps((client, "get")))
	geted, addr = s.recvfrom(1024)
	con = pickle.loads(geted)
	print(con)
	s.close()
	
	s = socket.socket() 
	s.connect(con)
	
	rT = threading.Thread(target=receving, args=(key, s))
	rT.start()
	
	print("Ready for chat!")
	
	mes = input()#"-> "
	while mes != 'q':
		s.send(encrypting(mes.encode(), key))
		mes = input()#"-> "
	s.send(mes.encode())
	s.close()
	print("Canceled")

def client_reciving(ip, port):
	global white_server
	key = "paymerespect"
	
	s = socket.socket() 
	s.connect(white_server)
	name = input("Enter your name: ")
	s.send(pickle.dumps((name,"reg", str(port))))
	s.close()
	
	print("Waiting connection")
	
	s = socket.socket()
	s.bind((ip, port))
	s.listen(10)
	c, addr = s.accept()
	
	rT = threading.Thread(target=receving, args=(key, c))
	rT.start()
	
	print("Ready for chat!")

	mes = input()#"-> "
	while mes != 'q':
		s.send(encrypting(mes.encode(), key))
		mes = input()#"-> "
	s.send(mes.encode())
	s.close()
	c.close()
	print("Canceled")

def via_node(ip, port):
	global white_server
	key = "paymerespect"
	
	s = socket.socket()
	s.connect((ip, port))
	name = input("Enter your name: ")
	s.send(name.encode())
	
	geted, addr = s.recvfrom(1024)
	print(geted.decode())
	
	rT = threading.Thread(target=receving, args=(key, s))
	rT.start()
	
	mes = input()#"-> "
	while mes != 'q':
		s.send(encrypting(mes.encode(), key))
		mes = input()#"-> "
	s.send(mes.encode())
	s.close()
	print("Canceled")

for ifaceName in interfaces():
	addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
	if "192.168.1" in ', '.join(addresses):
		ip = ', '.join(addresses)

way = input("Connecting (1) / reciving (2) / via node (3): ")
if way == '1':
	client_connecting(ip, 1024)
elif way == '2':
	client_reciving(ip, 1024)
else:
	s = socket.socket() 
	s.connect(white_server)
	s.send(pickle.dumps(("get_nodes")))
	data, addr = s.recvfrom(1024)
	nodes = pickle.loads(data)
	s.close()
	print(nodes)
	
	node = input("Enter node ip: ")
	via_node(node, nodes[node])
