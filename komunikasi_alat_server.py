import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4444        # The port used by the server

def listener_hl7():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        ssocket, addr = s.accept() #ssocket stands for server socket
        with ssocket:
            print('Connected to ', addr)
            while True:
                data = ssocket.recv(1024)
                if not data:
                    break
                ssocket.sendall(data)
    return data
        
if __name__ == '__main__':
    listener_hl7()
    

