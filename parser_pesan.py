import hl7
import mysql.connector
from datetime import datetime

'''Berikut merupakan API yang berfungsi sebagai parser pesan HL7 dan 
penghubung pesan antara alat lab dengan web app atau basis data. 
API ini hanya mengakomodasi pesan ORU_R01 '''

def parse_message(mes):
    '''Function that produce a parsed version of the HL7 message given'''
    return hl7.parse(mes, encoding='latin1')

def message_length(parsed_mes):
    '''Function that produce an output of the length of the parsed HL7 message or HL7 message segment'''
    return len(parsed_mes)

def parse_msh(parsed_mes):
    '''Function that parse MSH segment into dictionary that 
    contains all the message as the value with the name of the message as the key'''
    len_msh = message_length(parsed_mes[0]) #Give the length of the msh segment message
    if len_msh > 3 :
        incoming_mes = { #Input all the message as string into the dictionary
            "sending_application" : str(parsed_mes[0][3]),
            "sending_facility" : str(parsed_mes[0][4]),
            "recieving_application" : str(parsed_mes[0][5]),
            "recieving_facility" : str(parsed_mes[0][6]),
            "timestamp" : str(datetime.strptime(str(parsed_mes[0][7]), "%Y%m%d%H%M%S%f")),
            "security" : str(parsed_mes[0][8]),
            "message_type" : str(parsed_mes[0][9]),
            "control_id" : str(parsed_mes[0][10])}
    else:
        return print('There is no message')
    return incoming_mes 

def parse_pid(parsed_mes):
    '''Function that parse PID segment into dictionary that 
    contains all the message as the value with the name of the message as the key'''
    len_pid = message_length(parsed_mes[0]) #Give the length of the PID segment message
    if len_pid > 3 :
        incoming_mes = { #Input all the message as string into the dictionary
            "patient_id" : str(parsed_mes[1][2]),
            "patient_identifier" : str(parsed_mes[1][3]),
            "patient_id_alt" : str(parsed_mes[1][4]),
            "patient_name" : str(parsed_mes[1][5]),
            "mother_name" : str(parsed_mes[1][6]),
            "birth_date" : str(datetime.strptime(str(parsed_mes[1][7]), "%Y%m%d")),
            "sex" : str(parsed_mes[1][8]),
            "patient_alias" : str(parsed_mes[1][9]),
            "patient_race" : str(parsed_mes[1][10]),
            "patient_address" : str(parsed_mes[1][11]),
            "country_code" : str(parsed_mes[1][12]),
            "phone_number" : str(parsed_mes[1][13]),
            "business_number" : str(parsed_mes[1][14]),
            "languange" : str(parsed_mes[1][15])
            }
    else:
        return print('There is no message')
    return incoming_mes

def parse_obr(parsed_mes):
    '''Function that parse OBR segment into dictionary that 
    contains all the message as the value with the name of the message as the key'''
    len_obr = message_length(parsed_mes[2]) #Give the length of the OBR segment message
    if len_obr > 3 :
        incoming_mes = { #Input all the message as string into the dictionary
            "placer_order_number" : str(parsed_mes[2][2]),
            "filler_order_number" : str(parsed_mes[2][3]),
            "universal_service_id" : str(parsed_mes[2][4]),
            #"" : str(parsed_mes[2][5]),
            #"" : str(parsed_mes[2][6]),
            "obs_date" : str(datetime.strptime(str(parsed_mes[2][7]),"%Y%m%d")),
            #"obs_end_date" : str(datetime.strptime(str(parsed_mes[2][8]), "%Y%m%d")),
            "collection_vol" : str(parsed_mes[2][9]),
            "collection_id" : str(parsed_mes[2][10]),
            "danger_code" : str(parsed_mes[2][11]),
            "relevant_info" : str(parsed_mes[2][12]),
            #"" : str(datetime.strptime(str(parsed_mes[2][13]), "%Y%m%d")),
            #"" : str(parsed_mes[2][14]),
            #"" : str(parsed_mes[2][15]),
            #"" : str(parsed_mes[2][16]),
            #"" : str(parsed_mes[2][18])
            "result_status" : str(parsed_mes[2][25])
            }
    else:
        return print('There is no message')
    return incoming_mes

def parse_obx(parsed_mes):
    '''Function that parse OBX segment into dictionary that 
    contains all the message as the value with the name of the message as the key'''
    len_obx = message_length(parsed_mes[3]) #Give the length of the OBX segment message
    if len_obx > 3 :
        incoming_mes = { #Input all the message as string into the dictionary
            "value_type" : str(parsed_mes[3][2]),
            "obs_id" : str(parsed_mes[3][3]),
            "obs_sub_id" : str(parsed_mes[3][4]),
            "obs_value" : str(parsed_mes[3][5]),
            "units" : str(parsed_mes[3][6]),
            "ref_range" : str(parsed_mes[3][7]),
            #"birth_date" : str(datetime.strptime(str(parsed_mes[3][7]), "%Y%m%d")),
            "abnornal_flags" : str(parsed_mes[3][8]),
            "probabillity" : str(parsed_mes[3][8]),
            "nature_abnormal_test" : str(parsed_mes[3][9]),
            "obs_result_stat" : str(parsed_mes[3][10]),
            #"date_ref_range" : str(parsed_mes[3][11]),
            #"user_access" : str(parsed_mes[3][12]),
            #"obs_date" : str(datetime.strptime(str(parsed_mes[3][13]), "%Y%m%d")),
            #"producer_ref" : str(parsed_mes[3][14]),
            #"responsible_obs" : str(parsed_mes[3][15]),
            #"observation_method" : str(parsed_mes[3][16]),
            #"date_time_analysis" : str(parsed_mes[3][18])
            }
    else:
        return print('There is no message')
    return incoming_mes
   
if __name__ == '__main__':
    mes0 = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
    mes0 += 'PID|1||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|1962035|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
    mes0 += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||20020215||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
    mes0 += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\r'

    mes1 = 'MSH|^~\&|IA PHIMS Stage^2.16.840.1.114222.4.3.3.5.1.2^ISO|IA Public Health Lab^2.16.840.1.114222.4.1.10411^ISO|IA.DOH.IDSS^2.16.840.1.114222.4.3.3.19^ISO|IA DOH^2.16.840.1.114222.4.1.3650^ISO|201203142359||ORU^R01^ORU_R01|2.16.840.1.114222.4.3.3.5.1.2-20120314235954.325|T|2.5.1|||AL|NE|USA||||PHLabReport-Ack^^2.16.840.1.113883.9.10^ISO\r'
    mes1 += 'PID|1||14^^^IA PHIMS Stage&2.16.840.1.114222.4.3.3.5.1.2&ISO^PI^IA Public Health Lab&2.16.840.1.114222.4.1.10411&ISO||Finn^Huckleberry^^^^^L||19630815|M||2106-3^White^CDCREC^^^^04/24/2007~1002-5^American Indian or Alaska Native^CDCREC^^^^04/24/2007|721 SPRING STREET^^GRINNELL^IA^50112^USA^H|||||M^Married^HL70002^^^^2.5.1||||||H^Hispanic or Latino^HL70189^^^^2.5.1\r'
    mes1 += 'OBR|1||986^IA PHIMS Stage^2.16.840.1.114222.4.3.3.5.1.2^ISO|625-4^Bacteria identified in Stool by Culture^LN^^^^2.33^^Enteric Culture|||20120301|||||||||^SAWYER TOM MD^^^^^^^^L||||||201203140957|||P\r'
    mes1 += 'OBX|1|CWE|625-4^Bacteria identified in Stool by Culture^LN^^^^2.33^^result1|1|27268008^Salmonella^SCT^^^^20090731^^Salmonella species|||A^A^HL70078^^^^2.5|||P|||20120301|||^^^^^^^^Bacterial Culture||201203140957||||State Hygienic Laboratory^L^^^^IA Public Health Lab&2.16.840.1.114222.4.1.10411&ISO^FI^^^16D0648109|State Hygienic Laboratory^UI Research Park - Coralville^Iowa City^IA^52242-5002^USA^B^^19103|^Atchison^Christopher^^^^^^^L\r'

    mes = parse_message(mes0)
    msh = parse_msh(mes)
    print('total terdapat ' + str(len(mes)) + ' segment\n')
    pid = parse_pid(mes)
    obr = parse_obr(mes)
    obx = parse_obx(mes)
    print(msh)
    print("")
    print(pid)
    print("")
    print(obr)
    print("")
    print(obx)

    

    
