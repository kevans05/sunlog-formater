import glob
import csv

list_of_csv = glob.glob("/home/pi/Documents/sunlog/*.csv")
matches = ['RevenueGradeMeter: Solar Meter (#6, 13435)', 'Pac (W)']
list_to_csv = []
for csv_file in list_of_csv:
    print(csv_file)
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if not any (x in row for x in matches) :
                if len(row) != 0:
                    tem_dic = {"datetime":row[0],"Pac(W)":row[1],"Yield(Wh)":row[2],"Status":row[3],"Error":row[4],"Etotal_C(WattEver)":row[5],"Pac1(W)":row[6],"Pac2(W)":row[7],"Pac3(W)":row[8],"Uac1(V)":row[9],"Uac2 (V)":row[10],"Uac3 (V)":row[11], "Qac1 (var)":row[12],"Qac2 (var)":row[12],"Qac3 (var)":row[13], "Iac1 (mA)":row[14], "Iac2 (mA)":row[15], "Iac3 (mA)":row[16],"Fac (Hz)":row[17], "Cos(Phi)":row[18],"Pac raw (W)":row[19]}
                    list_to_csv.append(tem_dic)
            line_count += 1

print(list_to_csv)
keys = list_to_csv[0].keys()
with open('data.csv', 'w')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list_to_csv)
