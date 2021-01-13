import socket 
import threading
import pickle
from netifaces import interfaces, ifaddresses, AF_INET

tLock = threading.Lock()
def receving(sock_my, sock_connector):
    data = ' '
    try:
        while True and data != '':
            data, addr = sock_connector.recvfrom(1024)
            sock_my.send(data)
    except:
        pass

def redirect (ip, in_port, out_port):
	s1 = socket.socket()
	s1.bind((ip, in_port))
	s1.listen(10)
	c1, addr = s1.accept()
	data, addr = c1.recvfrom(1024)
	name = data.decode()
	
	s = socket.socket() 
	s.connect(('46.229.212.108', 54320))
	s.send(pickle.dumps((name,"reg", str(out_port))))
	s.close()
	
	c1.send("Waiting connection".encode())
	
	s2 = socket.socket()
	s2.bind((ip, out_port))
	s2.listen(10)
	c2, addr = s2.accept()
	
	rT = threading.Thread(target=receving, args=(c1, c2))
	rT.start()
	
	c1.send("Ready for chat!".encode())

	data = ' '
	try:
		while True and data != '':
			data, addr = c1.recvfrom(1024)
			c2.send(data)
	except:
		pass
	rT.join()
	c.close()

s = socket.socket() 
s.connect(('46.229.212.108', 54320))
s.send(pickle.dumps(("stun")))
data, addr = s.recvfrom(1024)
ip = data.decode()
s.close()

port = 1024

print(ip, port)

for ifaceName in interfaces():
	addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
	if "192.168.1" in ', '.join(addresses):
		ip = ', '.join(addresses)

redirect(ip, port, port*2)

while 1:
	pass