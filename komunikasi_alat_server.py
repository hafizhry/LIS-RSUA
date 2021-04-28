  
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5050        # The port used by the server

def listener_hl7():
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
        
        
if __name__ == '__main__':
    while True:
        mes = listener_hl7()
        print(mes)