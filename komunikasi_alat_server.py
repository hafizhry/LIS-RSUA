import socket
from _thread import *
import threading

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5050        # The port used by the server
#ThreadCount = 0

print_lock = threading.Lock()

def threaded(ssocket):
    while True:
        data = ssocket.recv(10240)
        print ("Server received data:", data)
        #return data.decode()
        if not data:
            print_lock.release()
            break
        ssocket.sendall(data)
    ssocket.close()

def listener_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print('Socket binded to port ', PORT)
        s.listen(5)
        print('Socket is listening')
        
        while True:
            ssocket, addr = s.accept() #ssocket stands for server socket
            print_lock.acquire()
            print('Connected to : ', addr[0], ' : ', addr[1])
            start_new_thread(threaded, (ssocket,))
            #ThreadCount += 1
            retu
        s.close()
        
if __name__ == '__main__':
    while True:
        listener_server()
                

