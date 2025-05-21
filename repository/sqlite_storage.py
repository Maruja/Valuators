'''This sublcass will implemmtnte the methods from data_storage to be able to 
read and save from sqlite database (in memory), later on we will implement a more 
robust DB 
'''
from models.address import Address, Session
from repository.data_storage import DataStorage
from utils.file_reader import FileReader

class SqliteStorage(DataStorage):
    list_addresses_obj = []


    def __init__(self):
      self.session = Session()
      
        # Add some example data
      '''  
        address1 = Address(d_codigo=23000, d_asenta="Zona Central", D_mnpio="La Paz", d_estado="Baja California Sur", d_ciudad="La Paz")
        address2 = Address(d_codigo=44180, d_asenta="Mexicaltzingo", D_mnpio="Guadalajara", d_estado="Jalisco", d_ciudad="Guadalajara")

        session.add_all([address1, address2])
        session.commit()
        print("Data inserted IN SQLITE  successfully!!!!!!!.")
    '''
      
      #session.add_all(self.list_addresses_obj)
      #session.commit()
      #print("NEw data inserted in SQLITE")

    def save(self, address):
        self.session.add(address) #stage the object 
        self.session.commit() #save to DB


    def load(self):
        # Start a session
        #session = Session()

        # Query all persons
        db_addresses = session.query(Address).all()

        # Display the results
        for address in db_addresses:
            print(address)
        print("FINISHED printig all addresses $$$$$$$$$$$$")
            #print(f"CP: {address.dcodigo }, dasenta: {address.dsenta}, dmnpio: {address.D_mnpio}, destado: {address.d_estado}, dciudad: {address.dciudad}")
    