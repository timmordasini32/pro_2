from csv import writer #Quelle *1*

def to_csv(data_lst):
    with open(f'database.csv', 'a+', newline='', encoding='utf-8') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(data_lst)
