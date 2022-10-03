from pprint import pprint
import re
import csv

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
repl_pattern = r'+7(\2)\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# 1: выполните пункты 1-3 ДЗ


def fio_phone_repair(c_list):
    new_contacts = []
    for contact in c_list:
        fio = ' '.join(contact[0:3]).split(' ')
        c_changed = [fio[0], fio[1], fio[2], contact[3], contact[4], re.sub(pattern, repl_pattern, contact[5]), contact[6]]
        new_contacts.append(c_changed)
    return join_contacts(new_contacts)


def join_contacts(d_list):
    for i in d_list:
        for j in d_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
    j_list = []
    for card in d_list:
        if card not in j_list:
            j_list.append(card)
    return j_list


pprint(fio_phone_repair(contacts_list))

# код для записи файла в формате CSV
with open("phonebook.csv", "w", newline='', encoding='UTF-8') as f:
    datawriter = csv.writer(f, dialect='excel', delimiter=',')
    datawriter.writerows(fio_phone_repair(contacts_list))
