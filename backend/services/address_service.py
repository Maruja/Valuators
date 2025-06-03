#This service will handle searching methods for the address class
from repository.file_reader import FileReader
from repository.sqlite_storage import SqliteStorage
from models.address import Address

class AddressService():
    
    storage = SqliteStorage()
    #storage = FileReader()

    def __init__(self):    
        pass

    def add_address(self,data):
        new_address = Address(d_codigo=data['d_codigo'],d_asenta=data['d_asenta'],d_tipo_asenta=data['d_tipo_asenta'], D_mnpio=data['D_mnpio'], d_estado=data['d_estado'], d_ciudad=data['d_ciudad'], d_CP=data['d_CP'], c_estado=data['c_estado'], c_oficina=data['c_oficina'], c_CP=data['c_CP'], c_tipo_asenta=data['c_tipo_asenta'], c_mnpio=data['c_mnpio'], id_asenta_cpcons=data['id_asenta_cpcons'], d_zona=data['d_zona'], c_cve_ciudad=data['c_cve_ciudad'])
        self.storage.save(new_address)
        
    def print_all(self):
        return [address.to_dict() for address in self.storage.load()]
    

    def load_addresses(self):
        storage_file_reader = FileReader()
        list_addresses_cvs = storage_file_reader.load()
        print("PRINTINNGGGG!!!!!!!!!! what comes from STORAGE FILE READER !!!!!!!!!!")
        [print(address) for address in list_addresses_cvs]
        [self.add_address(address.to_dict() ) for address in list_addresses_cvs]
        return self.print_all()


    def search_by_CP(self, CP_to_search):
        #List COmprehension
        #list_of_CPs = [address for address in self.list_addresses_obj if address.get_d_codigo() == CP_to_search ]
        list_of_CPs = self.storage.query_by_CP(CP_to_search)
        return [ addres.to_dict() for addres in list_of_CPs]
    
    def search_by_Municipio(self, Municipio_to_search):
        #List Comprehension 
        #list_of_Municipios = [ address for address in self.list_addresses_obj if address.get_d_municipio() == Municipio_to_search ]
        list_of_Municipios = self.storage.query_by_Mnpio(Municipio_to_search)
        return [ address.to_dict() for address in list_of_Municipios ]
