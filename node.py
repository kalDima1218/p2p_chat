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
	
	c1.send("Ready for chat!")

	data = ' '
	try:
		while True and data != '':
			data, addr = c1.recvfrom(1024)
			c2.send(data)
	except:
		pass
	rT.join()
	c.close()

for ifaceName in interfaces():
	addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
	if "192.168.1" in ', '.join(addresses):
		ip = ', '.join(addresses)

threads = []

for i in range(1024, 32768):
	if i != 2950 and i != 5900 and i != 12649 and i != 17161 and i != 19386 and i != 20120 and i != 20397 and i != 21811 and i != 22936 and i != 23622 and i != 25297 and i != 25298:
		threads.append(threading.Thread(target=redirect, args=(ip, i, i*2)))
		threads[-1].start()

print(ip)

while 1:
	pass
