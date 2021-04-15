import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4444      # The port used by the server

def listener_hl7():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 4444))
        #s.sendall(b'Hello, world')
        data = s.recv(1024)
        while data:
            print('Received:', data.decode())
            data = s.recv(1024)
        s.close()
    return data

if __name__ == '__main__':
    listener_hl7()

