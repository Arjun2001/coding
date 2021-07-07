import socket
import json


def printdata(data):
    print("================")
    for i in data:
        print(i,"   ",data[i][0],"   ",data[i][1])
    print("================")

host = socket.gethostname()
port = 12000
BUFFER_SIZE = 1024

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))
tcpClient.send("connect".encode())
res = tcpClient.recv(BUFFER_SIZE).decode()


if(res == 'Invalid Connection Request'):
    printdata(res)
else:

    res = json.loads(res)
    printdata(res)
    credentials = {}
    credentials['Name'] = input('Name: ')
    credentials['Email'] = input('Email: ')
    tcpClient.send(json.dumps(credentials).encode())

    response = tcpClient.recv(BUFFER_SIZE).decode()

    if(response == 'Invalid Credentials!'):
        print(response)
    else:
        print(response)
        order = input('Select a product: ')
        tcpClient.send(order.encode())
        orderResp = tcpClient.recv(BUFFER_SIZE).decode()
        tcpClient.send("connect".encode())
        if(orderResp.split(':')[0] == "Error"):
            print(orderResp.split(':')[1])
        else:
            print(orderResp.split(':')[1])
        result = tcpClient.recv(BUFFER_SIZE).decode()
        print(result.split(':')[1])
tcpClient.close()