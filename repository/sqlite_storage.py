'''This sublcass will implemmtnte the methods from data_storage to be able to 
read and save from sqlite database (in memory), later on we will implement a more 
robust DB 
'''
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from models.address import Address, Base
from repository.data_storage import DataStorage


# Connects to the database
engine = create_engine('sqlite:///repository/example.db', echo=True)
# Creates tables if they dont exist
Base.metadata.create_all(engine)
# Prepares a way to create Sessions
Session = sessionmaker(bind=engine)

#just to check if table was created
inspector = inspect(engine)
print("DATABASE !!!!!!!!", inspector.get_table_names())



class SqliteStorage(DataStorage):
    list_addresses_obj = []

    def __init__(self):
      self.session = Session()

    def save(self, address):
        self.session.add(address) #stage the object 
        self.session.commit() #save to DB


    def load(self):
        # Start a session
        #session = Session()

        # Query all persons
        db_addresses = Session.query(Address).all()

        # Display the results
        for address in db_addresses:
            print(address)
        print("FINISHED printig all addresses $$$$$$$$$$$$")
            #print(f"CP: {address.dcodigo }, dasenta: {address.dsenta}, dmnpio: {address.D_mnpio}, destado: {address.d_estado}, dciudad: {address.dciudad}")
    