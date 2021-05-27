import socket
from _thread import *
import threading
from parser_pesan_astm import *
from parser_pesan_hl7 import *

HOST = '127.0.0.1'  # IP address dari host
PORT = 5050        # port yang akan digunakan sebagai server/listener

print_lock = threading.Lock() # inisialisasi lock untuk thread
ThreadCount = 0 # variabel pemantau thread yang menyala

def threaded(ssocket):
    '''Fungsi ini melakukan inisiasi thread apabila terdapat pesan ASTM atau HL7 yang
    diterima oleh listener. Menerima masukan berupa socket yang telah terkoneksi dengan 
    port. Setelah itu pesan yang diterima oleh thread ini akan diteruskan ke parser ASTM atau HL7
    tergantung format pesan yang diterima'''
    while True:
        print('Thread terbuka')
        global ThreadCount
        data = ssocket.recv(102400) # menerima pesan
        
        if not data: # apabila tidak ada pesan yang diterima akan mengeluarkan pesan 
            print('Tidak ada data yang diterima')
            print_lock.release()
            ThreadCount -= 1
            break
        else:
            pass

        print ("Listener menerima pesan:")  
        print(data.decode('utf-8'))
        incoming_mes = data.decode('utf-8')
        if incoming_mes.split('|')[0] == 'MSH':
            parse_message_hl7(incoming_mes) # melakukan parsing untuk pesan HL7
            print_lock.release()
            ThreadCount -= 1
            break
        elif incoming_mes.split('|')[0] == 'H':
            parse_message_astm(incoming_mes) # melakukan parsing untuk pesan ASTM 
            print_lock.release()
            ThreadCount -= 1
            break
        else:
            print('Format pesan tidak sesuai')
            print_lock.release()
            ThreadCount -= 1
            break  

    ssocket.close()
    print('Thread ditutup\n')

def listener_server():
    '''Fungsi ini merupakan listener dari pesan ASTM dan HL7 dari instrumen laboratorium.
    Fungsi ini tidak menerima masukan apapun dan tidak menghasilkan luaran apapun, melainkan
    akan berjalan seterusnya hingga terdapat perintah untuk exit.
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try :
            s.bind((HOST, PORT))
        except socket.error as e:
            print(str(e))
        
        print('Socket terhubung ke port', PORT)
        s.listen(5)
        print('Socket siap menerima pesan')
        
        while True:
            ssocket, addr = s.accept() #ssocket adalah server socket
            print_lock.acquire()
            print('Terhubung ke :', addr[0], ':', addr[1]) 
            start_new_thread(threaded, (ssocket,))
            global ThreadCount
            ThreadCount += 1
            print('Thread nomor : ' + str(ThreadCount))
        s.close()
        
if __name__ == '__main__':
    while True:
        listener_server()
         