'''This code is to read the file CPdescarga.txt where all the CP's of Mexico are
This code will read and then separate each CP as an Object making all the fields 
an attribute of the class. 
'''
import glob
import csv
import os
from models.address import Address
from repository.data_storage import DataStorage



class FileReader(DataStorage):
    list_addresses_obj = []

    def __init__(self):
        pass          
    
    #function to read the file in parts for csv's for each state
    def load(self):
        #files = ['utils/CPdescarga_Jalisco.csv','utils/CPdescarga_BajaCaliforniaSur.csv']
        files = glob.glob(os.path.join('utils/', 'CPdescarga_*.csv'))

        for file in files:
            with open(file, mode='r', encoding='utf-8') as file_csv:
                reader = csv.DictReader(file_csv)
                i = 1
                for row in reader:
                    #print(i,row)
                    address = Address(row['d_codigo'],row['d_asenta'],row['d_tipo_asenta'],row['D_mnpio']
                                    ,row['d_estado'],row['d_ciudad'],row['d_CP'],row['c_estado']
                                    ,row['c_oficina'],row['c_CP'],row['c_tipo_asenta'],row['c_mnpio']
                                    ,row['id_asenta_cpcons'],row['d_zona'],row['c_cve_ciudad'])
                    self.list_addresses_obj.append(address)
                    i = i + 1
        return self.list_addresses_obj
    
    def save(self, address):
        pass
    

#function to read the file as a whole all mexico
def get_addresses_from_one_file_txt(self):
        file = 'utils/CPdescarga_test.txt'
        with open(file , 'r', ) as f:
            i=1
            for line in f:              
                list_words = line.split('|')
            
                address = Address(list_words[0],list_words[1],list_words[2],list_words[3],list_words[4],
                            list_words[5],list_words[6],list_words[7],list_words[8],list_words[9],
                            list_words[10],list_words[11],list_words[12],list_words[13],list_words[14])
                self.list_addresses_obj.append(address)
                print(i , address)
                i = i + 1 
            return self.list_addresses_obj
