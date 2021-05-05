import socket
from _thread import *
import threading
from parser_pesan_astm import *
from parser_pesan_hl7 import *

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5050        # The port used by the server


def threaded(ssocket, list_messages):
    while True:
        data = ssocket.recv(10240)
        print ("Server received data:", data.decode('utf-8'))
        #list_messages.append(data.decode('utf-8'))

        incoming_mes = data.decode('utf-8')
        if incoming_mes.split('|')[0] == 'MSH':
            parse_message_hl7(incoming_mes)
        elif incoming_mes.split('|')[0] == 'H':
            parse_message_astm(incoming_mes)
        else:
            print('Format error')

        if not data:
            break
    ssocket.close()
    print('Socket closed')

def listener_server():
    ThreadCount = 0
    list_messages=[]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print('Socket binded to port', PORT)
        s.listen(5)
        print('Socket is listening')
        
        while True:
            ssocket, addr = s.accept() #ssocket stands for server socket
            print('Connected to :', addr[0], ':', addr[1])
            start_new_thread(threaded, (ssocket,list_messages))
            ThreadCount += 1
            print('Thread Number : ' + str(ThreadCount))
            #print(list_messages)
        s.close()
    #return list_messages
        
if __name__ == '__main__':
    while True:
        listener_server()
         