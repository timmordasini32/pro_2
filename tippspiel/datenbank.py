# Erstellung des database. Hinterlegung der eingetragenen Werte in der Liste. Einträge in der Datenliste sollen auf einer neuen Zeile erscheinen und die Datenliste soll nicht jedesmal neu Überschrieben werden.
#Quelle *1*
from csv import writer

def to_csv(data_lst):
    with open(f'database.csv', 'a+', newline='', encoding='utf-8') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(data_lst)


# Quelle *1*: https://realpython.com/python-csv/

