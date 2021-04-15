import hl7
import mysql.connector
from datetime import datetime
from mysql.connector import Error, connect
from getpass import getpass
from parser_pesan import *
from komunikasi_database import *
from komunikasi_alat_client import *
from komunikasi_alat_server import *

if __name__ == '__main__':
    mes = listener_hl7()
    pid = parse_pid(mes)

    my_db = CONNECT_db()
    INSERT_db(pid, my_db, 'pid')
    my_db.commit()
