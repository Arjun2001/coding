import socket
import json
from threading import Thread

TCP_IP = '0.0.0.0'  
TCP_PORT = 12000
BUFFER_SIZE = 1024 
menu = {
    "A": [100, 10],
    "B": [500, 30],
    "C": [1000, 5]
}
orid = 1

class ClientThread(Thread):

    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print ("New socket thread started")

    def run(self):
        global menu, orid, BUFFER_SIZE
        ini = conn.recv(BUFFER_SIZE).decode()

        if(ini != 'connect'):
           conn.send("Invalid Connection".encode())
           return

        conn.send(json.dumps(menu).encode())
        cred = conn.recv(BUFFER_SIZE).decode()
        credDict = json.loads(cred)

        if(credDict.get('Name',0) and credDict.get('Email',0)):
            conn.send("Registration Successful!".encode())
        else:
            conn.send("Invalid Credentials!".encode())
            return

        order = conn.recv(BUFFER_SIZE).decode().split()

        if(len(order)%2 != 0):
            conn.send("Error:Invalid Order!".encode())
            return

        total = 0
        submenu = menu.copy()

        for i in range(0,len(order),2):
            item = submenu.get(order[i],0)

            if(item):
                if(item[1] >= int(order[i+1])):
                    total += item[0]*int(order[i+1])
                    submenu[order[i]][1] -= int(order[i+1])
                else:
                    conn.send("Error:Required quantity of {} not available".format(order[i]).encode())
                    return
            else:
                conn.send("Error:{} not available".format(order[i]).encode())
                return

        conn.send("Success:Amount payable = {}".format(total).encode())
        conn.recv(BUFFER_SIZE).decode()
        conn.send("Success:Ordered successfully through COD and your order id = {}".format(orid).encode())
        orid += 1
        menu = submenu.copy()

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:

    try:
        tcpServer.listen(4)
        print ("Waiting for the connection from clients")
        (conn, (ip,port)) = tcpServer.accept()
        newthread = ClientThread(ip,port)
        newthread.start()
        threads.append(newthread)
    except:
        print('Shutting down server!')
        break

for t in threads:
    t.join()