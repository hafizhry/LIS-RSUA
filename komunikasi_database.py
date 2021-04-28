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
            database='lis' # database=input('Enter database name:')
            )
        print('Connected to database')
        return connected_db
    except Error as e:
        return print(e)
    
'''def CHECK_COL_db():
    Function that checks whether the column of the data is exists within the database. 
    If the column doesn't exist, then the function will make a column from the keys of the dictionary'''

def INSERT_db(mydict, db_name, db_table):
    '''Function that insert data into a database'''
    cursor = db_name.cursor()
    
    placeholders = ', '.join(['%s'] * len(mydict))
    columns = ', '.join(mydict.keys())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (db_table, columns, placeholders)
    cursor.execute(sql, list(mydict.values()))
    print(sql)

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
