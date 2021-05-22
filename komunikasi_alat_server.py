import socket
from _thread import *
import threading
from parser_pesan_astm import *
from parser_pesan_hl7 import *

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5050        # The port used by the server

print_lock =threading.Lock()

def threaded(ssocket):
    while True:
        data = ssocket.recv(10240)
        if not data:
            print('Data missing')
            print_lock.release()
            break

        print ("Server received data:", data.decode('utf-8'))
        incoming_mes = data.decode('utf-8')
        if incoming_mes.split('|')[0] == 'MSH':
            parse_message_hl7(incoming_mes)
            print_lock.release()
            break
        elif incoming_mes.split('|')[0] == 'H':
            parse_message_astm(incoming_mes)
            print_lock.release()
            break
        else:
            print('Format error')
            print_lock.release()
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
            print_lock.acquire()
            print('Connected to :', addr[0], ':', addr[1])
            start_new_thread(threaded, (ssocket,))
            ThreadCount += 1
            print('Thread Number : ' + str(ThreadCount))
        s.close()
        
if __name__ == '__main__':
    while True:
        listener_server()
         