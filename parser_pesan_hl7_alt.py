import hl7
from datetime import datetime
from komunikasi_database import *

'''Berikut merupakan API yang berfungsi sebagai parser pesan HL7 dan 
penghubung pesan antara alat lab dengan web app atau basis data. 
API ini hanya mengakomodasi pesan ORU_R01 '''

def is_empty(string):
    '''Fungsi ini melakukan pengecekan apakah kolom kosong atau tidak.
    Apabila kolom kosong akan menghasilkan luaran True, selain itu akan menghasilkan luaran False'''
    if string == "":
        return True
    return False

def parse_message_hl7(mes):
    '''Fungsi ini menerima masukan berupa pesan HL7 dari instrumen laboratorium
    kemudian dilakukan parsing pesan memanfaatkan library hl7. Luaran dari fungsi
    ini adalah dictionary yang berisi informasi hasil parsing pesan HL7 berupa informasi
    barcode, nama pasien, tanggal lahir, jenis kelamin, parameter, nilai, satuan, dan penanda abnormal.'''
    
    parsed_mes = hl7.parse(mes, encoding='utf-8') # melakukan parsing menggunakan fungsi parse() dari library hl7
    incoming_mes = {
        "barcode" : str(parsed_mes[1][3]),
        "nama_pasien" : str(parsed_mes[1][5]).replace('^',' '),
        "tanggal_lahir" : str(datetime.strptime(str(parsed_mes[1][7]), "%Y%m%d").date()),
        "jenis_kelamin" : str(parsed_mes[1][8]),
        "parameter" : str(parsed_mes[3][3]),
        "nilai" : str(parsed_mes[3][5]).removeprefix('^'),
        "satuan" : str(parsed_mes[3][6]),
        "penanda_abnormal" : str(parsed_mes[3][8]),
    }

    if is_empty(incoming_mes['parameter']):
        incoming_mes["parameter"] = 'NULL'
    else:
        pass

    if is_empty(incoming_mes['nilai']):
        incoming_mes["nilai"] = 'NULL'
    else:
        pass

    if is_empty(incoming_mes['satuan']):
        incoming_mes["satuan"] = 'NULL'
    else:
        pass

    if is_empty(incoming_mes['penanda_abnormal']):
        incoming_mes["penanda_abnormal"] = 'NULL'
    else:
        pass

    print(incoming_mes) # menampilkan hasil parsing dalam bentuk dictionary
    try:
        INSERT_db(incoming_mes, 'hasil_alat')
    except Error as err:
        print(err)

   
if __name__ == '__main__':
    mes0 = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
    mes0 += 'PID|1||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|1962035|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
    mes0 += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||20020215||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
    mes0 += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\r'

    mes1 = 'MSH|^~\&|IA PHIMS Stage^2.16.840.1.114222.4.3.3.5.1.2^ISO|IA Public Health Lab^2.16.840.1.114222.4.1.10411^ISO|IA.DOH.IDSS^2.16.840.1.114222.4.3.3.19^ISO|IA DOH^2.16.840.1.114222.4.1.3650^ISO|201203142359||ORU^R01^ORU_R01|2.16.840.1.114222.4.3.3.5.1.2-20120314235954.325|T|2.5.1|||AL|NE|USA||||PHLabReport-Ack^^2.16.840.1.113883.9.10^ISO\r'
    mes1 += 'PID|1||14^^^IA PHIMS Stage&2.16.840.1.114222.4.3.3.5.1.2&ISO^PI^IA Public Health Lab&2.16.840.1.114222.4.1.10411&ISO||Finn^Huckleberry^^^^^L||19630815|M||2106-3^White^CDCREC^^^^04/24/2007~1002-5^American Indian or Alaska Native^CDCREC^^^^04/24/2007|721 SPRING STREET^^GRINNELL^IA^50112^USA^H|||||M^Married^HL70002^^^^2.5.1||||||H^Hispanic or Latino^HL70189^^^^2.5.1\r'
    mes1 += 'OBR|1||986^IA PHIMS Stage^2.16.840.1.114222.4.3.3.5.1.2^ISO|625-4^Bacteria identified in Stool by Culture^LN^^^^2.33^^Enteric Culture|||20120301|||||||||^SAWYER TOM MD^^^^^^^^L||||||201203140957|||P\r'
    mes1 += 'OBX|1|CWE|625-4^Bacteria identified in Stool by Culture^LN^^^^2.33^^result1|1|27268008^Salmonella^SCT^^^^20090731^^Salmonella species|||A^A^HL70078^^^^2.5|||P|||20120301|||^^^^^^^^Bacterial Culture||201203140957||||State Hygienic Laboratory^L^^^^IA Public Health Lab&2.16.840.1.114222.4.1.10411&ISO^FI^^^16D0648109|State Hygienic Laboratory^UI Research Park - Coralville^Iowa City^IA^52242-5002^USA^B^^19103|^Atchison^Christopher^^^^^^^L\r'

    parse_message_hl7(mes0)

    

    
