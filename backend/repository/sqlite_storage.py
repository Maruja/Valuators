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

    def __init__(self):
      self.session = Session()

    def save(self, address):
        self.session.add(address) #stage the object 
        self.session.commit() #save to DB

    def load(self):
        db_addresses = self.session.query(Address).all()
        return db_addresses
    
    def query_by_CP(self, search_d_codigo):
        addresses_cp = self.session.query(Address).filter(Address.d_codigo == search_d_codigo).all()
        return addresses_cp
    
    def query_by_Mnpio(self, search_D_Mnpio):
        addresses_Mnpio = self.session.query(Address).filter(Address.D_mnpio == search_D_Mnpio).all()
        return addresses_Mnpio