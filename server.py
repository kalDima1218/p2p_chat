import socket
import pickle

s = socket.socket()

host = 'SE.RV.ER.IP'
port = 54320

s.bind((host, port)) 
s.listen(10)

users = {}

while True: 
    c, addr = s.accept()
    print ('Got connection from', addr) 
    mes = pickle.loads(c.recv(1024))
    if str(mes[1]) == "reg":
        users[mes[0]] = (addr[0], int(mes[2]))
    elif str(mes[1]) == "get":
        try:
            c.send(pickle.dumps(users[mes[0]]))
        except:
            pass
    elif mes == "stun":
        c.send(addr[0].encode())
    c.close()
