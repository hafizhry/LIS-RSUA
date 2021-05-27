from datetime import datetime
from komunikasi_database import *


'''Berikut merupakan API yang berfungsi sebagai parser pesan ASTM dan 
penghubung pesan antara alat lab dengan web app atau basis data. 
API ini hanya mengakomodasi pesan ASTM dari dokumen ASTM E1394-97'''

def is_empty(string):
    '''Fungsi ini melakukan pengecekan apakah kolom kosong atau tidak.
    Apabila kolom kosong akan menghasilkan luaran True, selain itu akan menghasilkan luaran False'''
    if string == "":
        return True
    return False

def parse_message_astm(messages):  
    '''Fungsi ini menerima masukan berupa pesan ASTM dari instrumen laboratorium
    kemudian dilakukan parsing pesan dengan memanfaatkan fungsi splitlines() dan split()
    dari built-in library python. Luaran dari fungsi ini adalah dictionary yang berisi
    informasi hasil parsing pesan ASTM berupa barcode, nama pasien, tanggal lahir, 
    jenis kelamin, parameter, nilai, satuan, dan penanda abnormal.'''

    mes_split = [] # inisialisasi list
    incoming_mes = {"barcode" : [], # inisialisasi dictionary
            "nama_pasien" : [],
            "tanggal_lahir" : [],
            "jenis_kelamin" : [],
            "parameter" : [],
            "nilai" : [],
            "satuan" : [],
            "penanda_abnormal" : [],}

    mes_split = messages.splitlines() # membagi pesan ke dalam list berdasarkan baris

    for mes in mes_split: # melakukan rekursi untuk setiap pesan dalam list pesan
        if mes[0] == 'H':
            pass
        elif mes[0] == 'P':
            mes = mes.split('|') # membagi pesan ke dalam list berdasarkan karakter pipelines '|'
            incoming_mes['barcode'] = str(mes[4])
            incoming_mes['nama_pasien'] = str(mes[5].removeprefix('^').replace('^',' '))
            incoming_mes['tanggal_lahir'] = str(datetime.strptime(mes[7], "%Y%m%d").date())
            incoming_mes['jenis_kelamin'] = str(mes[8])
        elif mes[0] == 'C':
            pass
        elif mes[0] == 'O':
            pass
        elif mes[0] == 'R':
            mes = mes.split('|')
            incoming_mes['parameter'].append(str(mes[2].removeprefix('^^^^')))
            if is_empty(mes[3]):
                incoming_mes['nilai'].append('NULL')
            else:
                incoming_mes['nilai'].append(str(mes[3]))
                
            if is_empty(mes[4]):
                incoming_mes['satuan'].append('NULL')
            else:
                incoming_mes['satuan'].append(str(mes[4]))

            if is_empty(mes[6]):
                incoming_mes['penanda_abnormal'].append('NULL')
            else:
                incoming_mes['penanda_abnormal'].append(str(mes[6]))
        elif mes[0] == 'L':
            pass

    print(incoming_mes) # menampilkan hasil parsing dalam bentuk dictionary
    print('')
    try:
        INSERT_db(incoming_mes, 'hasil_alat')
    except Error as err:
        print(err)


if __name__ == '__main__':
    mes0 = 'H|¥^&|||XN-35^00-00^11001^^^^12345678||||||||E1394-97\r'
    mes0 += 'P|1|||123456|^Jim^Brown||20010820|M|||||^Dr.1||||||||||||^^^WEST\r'
    mes0 += 'Q|1|1^1^ ABCDE1234567890^B||||20010905150000||||||F\r'
    mes0 += 'O|1||^^ ABCDE1234567890^B|^^^^WBC¥^^^^RBC¥···¥^^^^BASO#|||||||N||||||||||||||F\r'
    mes0 += 'R|1|^^^^WBC^1|7.80|10*3/uL||N||||||20011116101000\r'

    mes1 = 'H|¥^&|||XN-550^00-01^11001^^^^12345678||||||||E1394-97\r'
    mes1 += 'P|1|||100|^Jim^Brown||20010820|M|||||^Dr.1||||||||||||^^^WEST\r'
    mes1 += 'C|1||Patient Comments\r'
    mes1 += 'O|1|2^1^ 1234567890^B||^^^^WBC¥^^^^RBC¥^^^^HGB¥^^^^HCT¥^^^^MCV¥^^^^MCH¥^^^^MCHC¥^^^^PLT¥^^^^NEUT%¥^^^^LYMPH%¥^^^^MONO%¥^^^^EO%¥^^^^BASO%¥^^^^NEUT#¥^^^^LYMPH#¥^^^^MONO#¥^^^^EO#¥^^^^BASO#¥^^^^RDW-SD¥^^^^RDW-CV¥^^^^PDW¥^^^^MPV¥^^^^P-LCR¥^^^^PCT||20010807101000|||||N||||||||||||||Q\r'
    mes1 += 'C|1||Sample Comments\r'
    mes1 += 'R|1|^^^^WBC^1^^^W|7.81|10*3/uL||N||||||20010806120000\r'
    mes1 += 'R|2|^^^^RBC^1|----|10*6/uL||A||||||20010806120000\r'
    mes1 += 'R|3|^^^^HGB^1|20.5|g/dL||W||||||20010806120000\r'
    mes1 += 'R|4|^^^^HCT^1|40.3|%||W||||||20010806120000\r'
    mes1 += 'R|33|^^^^PLT_Abn_Distribution||||A||||||20010806120000\r'
    mes1 += 'R|34|^^^^Blasts?|0||||||||||20010806120000\r'
    mes1 += 'R|35|^^^^Immature_Gran?|40||||||||||20010806120000\r'
    mes1 += 'R|36|^^^^Left_Shift?|0||||||||||20010806120000\r'
    mes1 += 'R|37|^^^^Atypical_Lympho?|0||||||||||20010806120000\r'
    mes1 += 'R|38|^^^^RBC_Lyse_Resistance?|10||||||||||20010806120000 \r'
    mes1 += 'R|39|^^^^Abn_Lympho/Blasts?|100|||A||||||20010806120000\r'
    mes1 += 'R|46|^^^^ACTION_MESSAGE_Delta||||A\r'
    mes1 += 'R|47|^^^^SCAT_DIFF|PNG&R&20010806&R&2001_08_06_12_00_1234567890_DIFF.PNG|||N||||||20010806120000\r'
    mes1 += 'L|1|N\r'

    parse_message_astm(mes0)



