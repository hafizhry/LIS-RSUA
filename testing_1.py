import hl7
import mysql.connector
from datetime import datetime
from mysql.connector import Error, connect
from getpass import getpass
from parser_pesan_hl7 import *
from komunikasi_database import *
from komunikasi_alat_client import *
from komunikasi_alat_server import *

if __name__ == '__main__':
    while True:
        mes = listener_hl7()
        print('Recieved mes')
        print(mes)
        mesHL7 = parse_message(mes)
        #pid = parse_pid(mesHL7)

        my_db = CONNECT_db()
        INSERT_db(mesHL7, my_db, 'result_tes')
        my_db.commit()
