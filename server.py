import socket
import pickle

s = socket.socket()

host = '46.229.212.108'
port = 54320

s.bind((host, port)) 
s.listen(10)

users = []
hosts = []

def find_user(user):
    for x,i in enumerate(users):
        if str(i) == str(user):
            return hosts[x]

while True: 
    c, addr = s.accept()
    print ('Got connection from', addr) 
    mes = pickle.loads(c.recv(1024))
    if str(mes[1]) == "reg":
        users.append(mes[0])
        hosts.append((addr[0], int(mes[2])))
    if str(mes[1]) == "get":
        print(find_user(mes[0]))
        c.send(pickle.dumps(find_user(mes[0])))
    print("Connection closed")
    
    c.close()
