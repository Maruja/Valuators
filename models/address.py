'''this class will be the base class for saving a complete address from CP ... all the way to id_city
d_codigo,d_asenta,d_tipo_asenta,D_mnpio,d_estado,d_ciudad,d_CP,c_estado,c_oficina,c_CP,c_tipo_asenta,c_mnpio,id_asenta_cpcons,d_zona,c_cve_ciudad
'''

from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.orm import declarative_base, sessionmaker

# Create an SQLite database (it will create a file named 'example.db')
engine = create_engine('sqlite:///repository/example.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)





class Address(Base):

    counter_address = 0

    __tablename__ = 'addresses'
    id_address = Column(Integer, primary_key=True)
    d_codigo = Column(Integer, nullable=False)
    d_asenta = Column(String(100), nullable=False)
    D_mnpio = Column(String(100), nullable=False)
    d_estado = Column(String(100), nullable=False)
    d_ciudad = Column(String(100), nullable=False)



    def __init__(self, d_codigo="",d_asenta="",d_tipo_asenta="",D_mnpio="",d_estado="",d_ciudad="",d_CP="",c_estado="",c_oficina="",c_CP="",c_tipo_asenta="",c_mnpio="",id_asenta_cpcons="",d_zona="",c_cve_ciudad=""):
        Address.counter_address += 1
        self.id_address = Address.counter_address
        self.d_codigo = d_codigo
        self.d_asenta = d_asenta
        self.d_tipo_asenta = d_tipo_asenta
        self.D_mnpio = D_mnpio
        self.d_estado = d_estado
        self.d_ciudad = d_ciudad
        self.d_CP = d_CP
        self.c_estado = c_estado
        self.c_oficina = c_oficina
        self.c_CP = c_CP
        self.c_tipo_asenta = c_tipo_asenta
        self.c_mnpio = c_mnpio
        self.id_asenta_cpcons = id_asenta_cpcons
        self.d_zona = d_zona
        self.c_cve_ciudad = c_cve_ciudad

    def get_id_address(self):
        return self.id_address

    def get_d_codigo(self):
        return self.d_codigo
    
    def get_d_estado(self):
        return self.d_estado
    
    def get_d_municipio(self):
        return self.D_mnpio

    def __repr__(self):
        return f"Address\n,ID address: {self.id_address}, Codigo Postal: {self.d_codigo}, Colonia: {self.d_asenta},  Municipio: {self.D_mnpio},Estado: {self.d_estado}, Ciudad: {self.d_ciudad}" 
    
    def to_dict(self):
        return { 
            "ID address" : self.id_address,
            " Codigo Postal" : self.d_codigo,
            " Colonia" : self.d_asenta,
            " Municipio" : self.D_mnpio,
            " Estado" : self.d_estado, 
            " Ciudad" : self.d_ciudad
        }
    
# Create the table (this needs to be outside the class)
Base.metadata.create_all(engine)
    
engine = create_engine('sqlite:///repository/example.db')
inspector = inspect(engine)

print("DATABASE !!!!!!!!", inspector.get_table_names())