  
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5050        # The port used by the server


def threaded(ssocket, list_messages):
    while True:
        data = ssocket.recv(10240)
        print ("Server received data:", data.decode('utf-8'))
        list_messages.append(data.decode('utf-8'))
        if not data:
            break
    ssocket.close()
    print('Socket closed')

def listener_server():
    ThreadCount = 0
    list_messages=[]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        ssocket, addr = s.accept() #ssocket stands for server socket
        with ssocket:
            s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
            print('Connected to ', addr)
            while True:
                data = ssocket.recv(10240)
                return data.decode()
                if not data:
                    break
                ssocket.sendall(data.decode())
        
        while True:
            ssocket, addr = s.accept() #ssocket stands for server socket
            print('Connected to : ', addr[0], ' : ', addr[1])
            start_new_thread(threaded, (ssocket,list_messages))
            ThreadCount += 1
            print('Thread Number : ' + str(ThreadCount))
            print(list_messages)
        s.close()
    
        
if __name__ == '__main__':
    while True:
        listener_server()
          

