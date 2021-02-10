import socket 
import threading
import pickle
from netifaces import interfaces, ifaddresses, AF_INET

white_server = ('46.229.212.108', 54320) #My server. You can use it for demo. Paste here your server ip to get MUCH SECURE

def receving(c1, c2):
    data = ' '
    try:
        while data != '' and data != b'q':
            data, addr = c1.recvfrom(1024)
            c2.send(data)
    except:
        pass
    c1.close()
    c2.close()

def redirect (ip, in_port, out_port):
	global white_server
	s1 = socket.socket()
	s1.bind((ip, in_port))
	s1.listen(10)
	
	s2 = socket.socket()
	s2.bind((ip, out_port))
	s2.listen(10)
	
	while True:
		s = socket.socket() 
		s.connect(white_server)
		s.send(pickle.dumps(("reg_node", in_port)))
		s.close()
		
		c1, addr = s1.accept()
		data, addr = c1.recvfrom(1024)
		name1 = data.decode()
		print("One")
		
		s = socket.socket() 
		s.connect(white_server)
		s.send(pickle.dumps(("reg_node", out_port)))
		s.close()
		
		c2, addr = s2.accept()
		data, addr = c2.recvfrom(1024)
		name2 = data.decode()
		print("Two")
		
		c1.send((name2 + " joined the chat!").encode())
		c2.send((name1 + " joined the chat!").encode())
	
		rT1 = threading.Thread(target=receving, args=(c1, c2))
		rT1.start()
		
		rT2 = threading.Thread(target=receving, args=(c2, c1))
		rT2.start()
		
		rT1.join()
		rT2.join()
		c1.close()
		c2.close()
		print("Canceled")
	s1.close()
	s2.close()

#s = socket.socket() 
#s.connect(white_server)
#s.send(pickle.dumps(("stun")))
#data, addr = s.recvfrom(1024)
#ip = data.decode()
#s.close()

port = 1024

#print(ip, port)

for ifaceName in interfaces():
	addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
	if "192.168.1" in ', '.join(addresses):
		ip = ', '.join(addresses)

redirect(ip, port, port*2)
