'''this class will be the base class for saving a complete address from CP ... all the way to id_city
d_codigo,d_asenta,d_tipo_asenta,D_mnpio,d_estado,d_ciudad,d_CP,c_estado,c_oficina,c_CP,c_tipo_asenta,c_mnpio,id_asenta_cpcons,d_zona,c_cve_ciudad
'''

class Address:

    def __init__(self, d_codigo="",d_asenta="",d_tipo_asenta="",D_mnpio="",d_estado="",d_ciudad="",d_CP="",c_estado="",c_oficina="",c_CP="",c_tipo_asenta="",c_mnpio="",id_asenta_cpcons="",d_zona="",c_cve_ciudad=""):
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

    def get_d_codigo(self):
        return self.d_codigo
    
    def get_d_estado(self):
        return self.d_estado
    
    def get_d_municipio(self):
        return self.D_mnpio

    def __repr__(self):
        return f"Address\n, Codigo Postal: {self.d_codigo}, Colonia: {self.d_asenta}, Estado: {self.d_estado}, Ciudad: {self.d_ciudad}, Municipio: {self.D_mnpio}" 
    
    def to_dict(self):
        return { 
            " Codigo Postal" : self.d_codigo,
            " Colonia" : self.d_asenta,
            " Estado" : self.d_estado, 
            " Ciudad" : self.d_ciudad,
            " Municipio" : self.D_mnpio
        }
    