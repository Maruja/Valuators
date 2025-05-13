#main place to run the Valuators app 
from flask import Flask, jsonify
from services.address_service import AddressService



app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Esto deshabilita el escape Unicode
address_service = AddressService()

# Endpoint principal
@app.route('/')
def hello_world():
    return '¡Hellllo Valuators app!'

#Printing all the addresses
@app.route('/C_P_code', methods=['GET'])
def print_all():
    CP_Codes = address_service.print_all()
    if CP_Codes:
        return jsonify(CP_Codes), 200
    return jsonify({"error": "NO CPs found !"}), 404

#Searching by CP will return all of the same CP
@app.route('/C_P_code/<cp>', methods=['GET'])
def search_by_cp(cp):
    response = address_service.search_by_CP(cp)
    if response :
        return jsonify(response), 200
    return jsonify({"error": "NO addresses found with this CP !"}), 400

#Searching by Municipio will return all of the same Municipio
@app.route('/Mnpio/<Municipio_to_search>', methods=['GET'])
def search_by_estado(Municipio_to_search):
    response = address_service.search_by_Municipio(Municipio_to_search)
    if response: 
        return jsonify(response), 200
    return jsonify({"error": "No Municipalities found"}), 400

    


# Endpoint con parámetro dinámico
@app.route('/saludo/<nombre>')
def saludo_personalizado(nombre):
    return f'¡Hola, {nombre}! Bienvenido al microservicio Flask 😊'

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
