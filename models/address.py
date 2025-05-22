'''this class will be the base class for saving a complete address from CP ... all the way to id_city
d_codigo,d_asenta,d_tipo_asenta,D_mnpio,d_estado,d_ciudad,d_CP,c_estado,c_oficina,c_CP,c_tipo_asenta,c_mnpio,id_asenta_cpcons,d_zona,c_cve_ciudad
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

#creates the table base like schema 
Base = declarative_base()

class Address(Base):

    __tablename__ = 'addresses'
    id_address = Column(Integer, primary_key=True, autoincrement=True)
    d_codigo = Column(Integer, nullable=False)
    d_asenta = Column(String(100), nullable=False)
    d_tipo_asenta = Column(String(100), nullable=False)
    D_mnpio = Column(String(100), nullable=False)
    d_estado = Column(String(100), nullable=False)
    d_ciudad = Column(String(100), nullable=False)    
    d_CP = Column(String(100), nullable=False)
    c_estado = Column(String(100), nullable=False)
    c_oficina = Column(String(100), nullable=False)
    c_CP = Column(String(100), nullable=False)
    c_tipo_asenta = Column(String(100), nullable=False)
    c_mnpio = Column(String(100), nullable=False)
    id_asenta_cpcons = Column(String(100), nullable=False)
    d_zona = Column(String(100), nullable=False)
    c_cve_ciudad = Column(String(100), nullable=False)


    def __init__(self, d_codigo="",d_asenta="",d_tipo_asenta="",D_mnpio="",d_estado="",d_ciudad="",d_CP="",c_estado="",c_oficina="",c_CP="",c_tipo_asenta="",c_mnpio="",id_asenta_cpcons="",d_zona="",c_cve_ciudad=""):
        #self.id_address = Ad
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
            "id_address" : self.id_address,
            "d_codigo" : self.d_codigo,
            "d_asenta" : self.d_asenta,
            "d_tipo_asenta" : self.d_tipo_asenta,        
            "D_mnpio" : self.D_mnpio,
            "d_estado" : self.d_estado, 
            "d_ciudad" : self.d_ciudad,
            "d_CP" : self.d_CP,
            "c_estado" : self.c_estado,
            "c_oficina" : self.c_oficina,
            "c_CP" : self.c_CP,
            "c_tipo_asenta" : self.c_tipo_asenta,
            "c_mnpio" : self.c_mnpio,
            "id_asenta_cpcons" : self.id_asenta_cpcons,
            "d_zona" : self.d_zona,
            "c_cve_ciudad" : self.c_cve_ciudad
        }
    
    
        
        