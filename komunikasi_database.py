import mysql.connector
from mysql.connector import Error, connect
from getpass import getpass

def CONNECT_db():
    '''Function that connect the API to a database'''
    try:
        connected_db = mysql.connector.connect(
            host='localhost', 
            user='root', # user=input('Enter username:'),
            password='', # password=getpass('Enter password:'),
            database='laravel_crud' # database=input('Enter database name:')
            )
        print('Connected to database')
        return connected_db
    except Error as e:
        return print(e)
    

def INSERT_db(mydict, db_name, db_table):
    '''Function that insert data into a database'''
    cursor = db_name.cursor()
    
    placeholders = ', '.join(['%s'] * len(mydict))
    columns = ', '.join(mydict.keys())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (db_table, columns, placeholders)
    cursor.execute(sql, list(mydict.values()))
    print(sql)

def INSERT_db_astm(mydict, db_name, db_table):
    cursor = db_name.cursor()
    temp_mydict = {}
    length = len(mydict['parameter'])
    if length > 1:
        idx = 0
        while idx < length-1:
            temp_mydict['barcode'] = mydict['barcode']
            temp_mydict['nama_pasien'] = mydict['nama_pasien']
            temp_mydict['jenis_kelamin'] = mydict['jenis_kelamin']
            temp_mydict['tanggal_lahir'] = mydict['tanggal_lahir']
            temp_mydict['parameter'] = mydict['parameter'][idx]
            temp_mydict['nilai'] = mydict['nilai'][idx]
            temp_mydict['satuan'] = mydict['satuan'][idx]
            temp_mydict['nilai_acuan'] = mydict['nilai_acuan'][idx]
            temp_mydict['penanda_abnormal'] = mydict['penanda_abnormal'][idx]
            print(temp_mydict)
            INSERT_db(temp_mydict, db_name, db_table)
            idx += 1


    else:
        temp_mydict['barcode'] = mydict['barcode']
        temp_mydict['nama_pasien'] = mydict['nama_pasien']
        temp_mydict['jenis_kelamin'] = mydict['jenis_kelamin']
        temp_mydict['tanggal_lahir'] = mydict['tanggal_lahir']
        temp_mydict['parameter'] = mydict['parameter'][0]
        temp_mydict['nilai'] = mydict['nilai'][0]
        temp_mydict['satuan'] = mydict['satuan'][0]
        temp_mydict['nilai_acuan'] = mydict['nilai_acuan'][0]
        temp_mydict['penanda_abnormal'] = mydict['penanda_abnormal'][0]
        print(temp_mydict)
        INSERT_db(temp_mydict, db_name, db_table)

    

if __name__ == '__main__':
    mes = {
        'nama_pasien' : 'ochid', 
        'id_pasien' : 1211,
        'parameter' : 113,
        'nilai' : 1311,
        'satuan' : 'dm/l',
        'nilai_acuan' : 1230
    }
    my_db = CONNECT_db()
        
    INSERT_db(mes, my_db, 'result_tes')
    #my_db.commit()
