#This service will handle searching methods for the address class
from utils.reader import Reader
from models.address import Address



class AddressService:
    list_addresses_obj = []

    def __init__(self):
        #self.list_addresses_obj = Reader().get_addresses_from_one_file_txt()
        self.list_addresses_obj = Reader().get_addresses_from_several_files_csv()

    def print_all(self):
        return [addres.to_dict() for addres in self.list_addresses_obj]

    def search_by_CP(self, CP_to_search):
        list_of_CPs = []
        for address in self.list_addresses_obj:
            if address.get_d_codigo() == CP_to_search:
                #print("Found a match")
                list_of_CPs.append(address)
        if list_of_CPs == []:
            return "FOUND NOTHING !!"
        return [ addres.to_dict() for addres in list_of_CPs]
    
    def search_by_Municipio(self, Municipio_to_search):
        list_of_Municipios = []
        for address in self.list_addresses_obj:
            if address.get_d_municipio() == Municipio_to_search:
                list_of_Municipios.append(address)
        if list_of_Municipios == []:
            return "FOUND NOTHING !!"
        return [ address.to_dict() for address in list_of_Municipios ]
