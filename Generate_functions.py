import pypict.tools
import csv

params = {
    "Show_Screen":	["1", "0"],
    "OplataOtmenaVozvrat":	["1", "0"],
    "Predavtorizacii":	["1", "0"],
    "Spasibo":	["1", "0"],
    "Valyuty":	["1", "0"],
    "Skidki":	["1", "0"],
    "Komissii/shtrafy":	["1", "0"],
    "CHaevye_odnoj_tranzakciej":	["1", "0"],
    "CHaevye_dvumya_tranzakciyami":	["1", "0"],
    "PZH":	["1", "0"],
    "noCVM_operacii":	["1", "0"],
    "Monitoring":	["1", "0"],
    "Loyal'nost'":	["1", "0"],
    "Toplivnye_karty":	["1", "0"],
    "Otdely":	["1", "0"],
    "Operacii_bez_karty":	["1", "0"],
    "Otchety":	["1", "0"],
    "Operacii_s_ruchnym_vvodom":	["1", "0"],
    "Operacii_bez_predyavleniya_karty":	["1", "0"],    #Operacii_bez_pred"yavleniya_karty > Operacii_bez_predyavleniya_karty
    "Sluzhebnye_operacii":	["1", "0"],
    "Udalennaya_zagruzka":	["1", "0"],
    "Negativnye_kejsy_UZ":	["1", "0"],
    "Negativnye_kejsy_oplaty":	["1", "0"],
    "NFC_PAY":	["1", "0"],
    "Cashout":	["1", "0"]
}

with open('Generate_functions.csv', 'w', newline='') as csvfile:
    fieldnames = params.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for case in pypict.tools.from_dict(params):
        print(case)
        writer.writeheader()
        writer.writerow(case)


