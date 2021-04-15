import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 4444        # The port used by the server

def sender_hl7(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        ssocket, addr = s.accept() #ssocket stands for server socket
        with ssocket:
            print('Connected to ', addr)
            ssocket.sendall(message.encode())
        ssocket.close()
        
if __name__ == '__main__':
    
    mes1 = 'MSH|^~\&|IA PHIMS Stage^2.16.840.1.114222.4.3.3.5.1.2^ISO|IA Public Health Lab^2.16.840.1.114222.4.1.10411^ISO|IA.DOH.IDSS^2.16.840.1.114222.4.3.3.19^ISO|IA DOH^2.16.840.1.114222.4.1.3650^ISO|201203142359||ORU^R01^ORU_R01|2.16.840.1.114222.4.3.3.5.1.2-20120314235954.325|T|2.5.1|||AL|NE|USA||||PHLabReport-Ack^^2.16.840.1.113883.9.10^ISO\r'
    mes1 += 'PID|1||14^^^IA PHIMS Stage&2.16.840.1.114222.4.3.3.5.1.2&ISO^PI^IA Public Health Lab&2.16.840.1.114222.4.1.10411&ISO||Finn^Huckleberry^^^^^L||19630815|M||2106-3^White^CDCREC^^^^04/24/2007~1002-5^American Indian or Alaska Native^CDCREC^^^^04/24/2007|721 SPRING STREET^^GRINNELL^IA^50112^USA^H|||||M^Married^HL70002^^^^2.5.1||||||H^Hispanic or Latino^HL70189^^^^2.5.1\r'
    mes1 += 'OBR|1||986^IA PHIMS Stage^2.16.840.1.114222.4.3.3.5.1.2^ISO|625-4^Bacteria identified in Stool by Culture^LN^^^^2.33^^Enteric Culture|||20120301|||||||||^SAWYER TOM MD^^^^^^^^L||||||201203140957|||P\r'
    mes1 += 'OBX|1|CWE|625-4^Bacteria identified in Stool by Culture^LN^^^^2.33^^result1|1|27268008^Salmonella^SCT^^^^20090731^^Salmonella species|||A^A^HL70078^^^^2.5|||P|||20120301|||^^^^^^^^Bacterial Culture||201203140957||||State Hygienic Laboratory^L^^^^IA Public Health Lab&2.16.840.1.114222.4.1.10411&ISO^FI^^^16D0648109|State Hygienic Laboratory^UI Research Park - Coralville^Iowa City^IA^52242-5002^USA^B^^19103|^Atchison^Christopher^^^^^^^L\r'

    sender_hl7(mes1)
    

