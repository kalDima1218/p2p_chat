import socket 
import threading
import pickle
from aes import encrypting, decrypting
from netifaces import interfaces, ifaddresses, AF_INET

tLock = threading.Lock()
def receving(key, sock):
    data = ' '
    try:
        while True and data != '':
            data, addr = sock.recvfrom(1024)
            print ('New message: '+ decrypting(data, key))
    except:
        pass

def client_connecting(ip, port):
    key = "paymerespect"
    s = socket.socket() 
    s.connect(('SE.RV.ER.IP', 54320))
    name = input("Enter your name: ")
    s.send(pickle.dumps((name, "reg", str(port))))
    s.close()
    
    s = socket.socket() 
    s.connect(('SE.RV.ER.IP', 54320))
    client = input("Enter client name: ")
    s.send(pickle.dumps((client, "get")))
    geted, addr = s.recvfrom(1024)
    con = pickle.loads(geted)
    s.close()
    
    s = socket.socket() 
    s.connect(con)
    
    rT = threading.Thread(target=receving, args=(key, s))
    rT.start()
    
    print("Ready for chat!")
    
    while True:
        mes = input()#"-> "
        s.send(encrypting(mes.encode(), key))
    rT.join()

def client_reciving(ip, port):
    key = "paymerespect"
    s = socket.socket() 
    s.connect(('SE.RV.ER.IP', 54320))
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

    while True:
        mes = input()#"-> "
        c.send(encrypting(mes.encode(), key))
    rT.join()
    c.close()

def via_node(ip, port):
    key = "paymerespect"
    s = socket.socket()
	
    s.connect((ip, port))
    name = input("Enter your name: ")
    s.send(name.encode())
    geted, addr = s.recvfrom(1024)
    print(geted.decode())
    geted, addr = s.recvfrom(1024)
    print(geted.decode())
    
    rT = threading.Thread(target=receving, args=(key, s))
    rT.start()
    
    while True:
        mes = input()#"-> "
        s.send(encrypting(mes.encode(), key))
    rT.join()

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
	node_ip = input("Enter node ip: ")
	via_node(node_ip, 1024)
s.close()
