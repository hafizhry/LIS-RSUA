import astm

mes0 = 'H|¥^&|||XN-35^00-00^11001^^^^12345678||||||||E1394-97\r'
mes0 += 'P|1|||123456|^Jim^Brown||20010820|M|||||^Dr.1||||||||||||^^^WEST\r'
mes0 += 'Q|1|1^1^ ABCDE1234567890^B||||20010905150000||||||F\r'
mes0 += 'O|1||^^ ABCDE1234567890^B|^^^^WBC¥^^^^RBC¥···¥^^^^BASO#|||||||N||||||||||||||F\r'
mes0 += 'R|1|^^^^WBC^1|7.80|10*3/uL||N||||||20011116101000\r'

mes1 = 'H|¥^&|||XN-550^00-01^11001^^^^12345678||||||||E1394-97<CR>\r'
mes1 += 'P|1|||100|^Jim^Brown||20010820|M|||||^Dr.1||||||||||||^^^WEST<CR>\r'
mes1 += 'C|1||Patient Comments<CR>\r'
mes1 += 'O|1|2^1^ 1234567890^B||^^^^WBC¥^^^^RBC¥^^^^HGB¥^^^^HCT¥^^^^MCV¥^^^^MCH¥^^^^MCHC¥^^^^PLT¥^^^^NEUT%¥^^^^LYMPH%¥^^^^MONO%¥^^^^EO%¥^^^^BASO%¥^^^^NEUT#¥^^^^LYMPH#¥^^^^MONO#¥^^^^EO#¥^^^^BASO#¥^^^^RDW-SD¥^^^^RDW-CV¥^^^^PDW¥^^^^MPV¥^^^^P-LCR¥^^^^PCT||20010807101000|||||N||||||||||||||Q<CR>\r'
mes1 += 'C|1||Sample Comments<CR>\r'
mes1 += 'R|1|^^^^WBC^1^^^W|7.81|10*3/uL||N||||||20010806120000\r'
mes1 += 'R|2|^^^^RBC^1|----|10*6/uL||A||||||20010806120000<CR>\r'
mes1 += 'R|3|^^^^HGB^1|20.5|g/dL||W||||||20010806120000<CR>\r'
mes1 += 'R|4|^^^^HCT^1|40.3|%||W||||||20010806120000<CR>\r'
mes1 += 'R|33|^^^^PLT_Abn_Distribution||||A||||||20010806120000<CR>\r'
mes1 += 'R|34|^^^^Blasts?|0||||||||||20010806120000<CR>\r'
mes1 += 'R|35|^^^^Immature_Gran?|40||||||||||20010806120000<CR>\r'
mes1 += 'R|36|^^^^Left_Shift?|0||||||||||20010806120000<CR>\r'
mes1 += 'R|37|^^^^Atypical_Lympho?|0||||||||||20010806120000<CR>\r'
mes1 += 'R|38|^^^^RBC_Lyse_Resistance?|10||||||||||20010806120000 <CR>\r'
mes1 += 'R|39|^^^^Abn_Lympho/Blasts?|100|||A||||||20010806120000<CR>\r'
mes1 += 'R|46|^^^^ACTION_MESSAGE_Delta||||A<CR>'
mes1 += 'R|47|^^^^SCAT_DIFF|PNG&R&20010806&R&2001_08_06_12_00_1234567890_DIFF.PNG|||N||||||20010806120000<CR>\r'
mes1 += 'L|1|N<CR>\r'

mes_split = []
mes_split = mes1.splitlines()
mes_split = [mes for line in mes_split for mes in line.split('|')]
print(mes_split)

'''mes_bytes = bytes(mes0, 'utf-8')
mes_astm = astm.codec.decode_record(mes_bytes,'utf-8')
print(mes_astm)'''