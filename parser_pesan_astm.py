import astm
from datetime import datetime
from komunikasi_database import *

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_null(string):
    if string == "":
        return True
    return False

def parse_message_astm(messages):  
    mes_split = []
    incoming_mes = {"barcode" : [],
            "nama_pasien" : [],
            "tanggal_lahir" : [],
            "jenis_kelamin" : [],
            "parameter" : [],
            "nilai" : [],
            "satuan" : [],
            "nilai_acuan" : [],
            "penanda_abnormal" : [],}

    mes_split = messages.splitlines()

    for mes in mes_split:
        if mes[0] == 'H':
            pass
        elif mes[0] == 'P':
            mes = mes.split('|')
            incoming_mes['barcode'] = int(mes[4])
            incoming_mes['nama_pasien'] = mes[5]
            incoming_mes['tanggal_lahir'] = str(datetime.strptime(mes[7], "%Y%m%d").date())
            incoming_mes['jenis_kelamin'] = mes[8]
        elif mes[0] == 'C':
            pass
        elif mes[0] == 'O':
            pass
        elif mes[0] == 'R':
            mes = mes.split('|')
            incoming_mes['parameter'].append(mes[2])

            if is_number(mes[3]):
                incoming_mes['nilai'].append(float(mes[3]))
            else:
                incoming_mes['nilai'].append('NULL')

            if is_null(mes[4]):
                incoming_mes['satuan'].append('NULL')
            else:
                incoming_mes['satuan'].append(mes[4])

            if is_null(mes[5]):
                incoming_mes['nilai_acuan'].append('NULL')
            else:
                incoming_mes['nilai_acuan'].append(mes[5])

            if is_null(mes[6]):
                incoming_mes['penanda_abnormal'].append('NULL')
            else:
                incoming_mes['penanda_abnormal'].append(mes[6])

        elif mes[0] == 'L':
            pass

    print(incoming_mes)
    my_db = CONNECT_db()
    INSERT_db_astm(incoming_mes, my_db, 'result')
    my_db.commit()


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

    parse_message_astm(mes1)



