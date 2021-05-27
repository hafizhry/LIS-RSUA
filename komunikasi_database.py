import mysql.connector
import mysql.connector.errors
from mysql.connector import  connect
from getpass import getpass
from mysql.connector.errors import DatabaseError, Error

def CONNECT_db():
    '''Fungsi ini digunakan untuk menghubungkan API ke basis data.
    Fungsi ini tidak menerima masukan dan tidak menghasilkan luaran.'''
    try:
        connected_db = mysql.connector.connect(
            host='45.130.230.201', 
            user='u1026039_silrsua',
            password='Apaajaboleh123!',
            database='u1026039_silrsua' 
            )
        # connected_db = mysql.connector.connect(
        #     host='localhost', 
        #     user='root',
        #     password='',
        #     database='laravel_crud2' 
        #     )
        print('Terkoneksi ke basis data')
        return connected_db
    except Error:
        raise
    

def INSERT_QUERY_db(mydict, db_table):
    '''Fungsi ini digunakan untuk memasukkan data ke dalam basis data.
    Data yang dimasukkan adalah data hasil parsing dari API'''
    db_name = CONNECT_db()
    cursor = db_name.cursor()
    
    placeholders = ', '.join(['%s'] * len(mydict))
    columns = ', '.join(mydict.keys())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (db_table, columns, placeholders)
    try:
        cursor.execute(sql, list(mydict.values()))
        print(sql)
        db_name.commit()
        db_name.close()
        print('Koneksi basis data tertutup')
    except Error:
        raise
      

def INSERT_db(mydict, db_table):
    temp_mydict = {}
    length = len(mydict['parameter'])
    if length > 1:
        idx = 0
        while idx <= length-1:
            temp_mydict['barcode'] = mydict['barcode']
            temp_mydict['nama_pasien'] = mydict['nama_pasien']
            temp_mydict['jenis_kelamin'] = mydict['jenis_kelamin']
            temp_mydict['tanggal_lahir'] = mydict['tanggal_lahir']
            temp_mydict['parameter'] = mydict['parameter'][idx]
            temp_mydict['nilai'] = mydict['nilai'][idx]
            temp_mydict['satuan'] = mydict['satuan'][idx]
            temp_mydict['penanda_abnormal'] = mydict['penanda_abnormal'][idx]
            print(temp_mydict)
            try:
                INSERT_QUERY_db(temp_mydict, db_table)
                idx += 1
            except Error:
                raise
    else:
        temp_mydict['barcode'] = mydict['barcode']
        temp_mydict['nama_pasien'] = mydict['nama_pasien']
        temp_mydict['jenis_kelamin'] = mydict['jenis_kelamin']
        temp_mydict['tanggal_lahir'] = mydict['tanggal_lahir']
        temp_mydict['parameter'] = mydict['parameter'][0]
        temp_mydict['nilai'] = mydict['nilai'][0]
        temp_mydict['satuan'] = mydict['satuan'][0]
        temp_mydict['penanda_abnormal'] = mydict['penanda_abnormal'][0]
        print(temp_mydict)
        try:
            INSERT_QUERY_db(temp_mydict, db_table)
        except Error:
            raise


    

# if __name__ == '__main__':
    # mes = {
    #     'nama_pasien' : 'ochid', 
    #     'id_pasien' : 1211,
    #     'parameter' : 113,
    #     'nilai' : 1311,
    #     'satuan' : 'dm/l',
    #     'nilai_acuan' : 1230
    # }
    # my_db = CONNECT_db()
        
    # INSERT_db(mes, my_db, 'result_tes')
    # my_db.commit()
