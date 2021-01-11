import socket 
import threading
import pickle
tLock = threading.Lock()
shutdown = False
def receving(name, sock):
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            print ('\nNew message: '+ str(data.decode()))
    except:
        pass
s = socket.socket() 
host = '46.229.212.108'
port = 54320

if input("First or second: ") == "1":
    s.connect((host,port))
    arr = ("client_1", "reg", "1024")
    s.send(pickle.dumps(arr))
    data, addr = s.recvfrom(1024)
    s.close()
    
    s = socket.socket() 
    s.connect((host,port))
    arr = ("client_2", "get")
    s.send(pickle.dumps(arr))
    geted, addr = s.recvfrom(1024)
    con = pickle.loads(geted)
    print(con)
    s.close()
    
    s = socket.socket() 
    s.connect((con))
    
    rT = threading.Thread(target=receving, args=("RecvThread",s))
    rT.start()
    
    mes = input("-> ")
    while mes != "Quite":
        s.send(mes.encode())
        mes = input("-> ")
else:
    s.connect((host,port))
    arr = ("client_2","reg", "1025")
    s.send(pickle.dumps(arr))
    s.close()
    
    s = socket.socket()
    s.bind(("192.168.1.49", 1025))
    s.listen(10)
    c, addr = s.accept()
    print ('Got connection from', addr) 
    
    rT = threading.Thread(target=receving, args=("RecvThread",c))
    rT.start()

    mes = input("-> ")
    while mes != "Quite":
        c.send(mes.encode())
        mes = input("-> ")
    rT.join()
    c.close()
s.close()
