import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5050      # The port used by the server

def sender_client(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode())
    print('Terkirim dari  ' + '(\'' +str(HOST) + '\', ' + str(PORT) + ')')
    print('Data berhasil terkirim!')
            
if __name__ == '__main__':
      
    mes0 = ''
    sender_client(mes0)