#main place to run the Valuators app 
from flask import Flask, jsonify, request
from services.address_service import AddressService
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')




app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Esto deshabilita el escape Unicode

logging.info("Loading address_service")
address_service = AddressService()
logging.info("address_service loaded")


# Endpoint principal
@app.route('/')
def hello_world():
    return '¡Hellllo Valuators app!'

#Saving one address
@app.route('/Address', methods=['POST'])
def save_address():
    data = request.get_json()
    
    # Validate required fields
    if not data or not data.get('d_codigo') or not data.get('d_asenta'):
        return jsonify({"error": "CP and Asentamiento are required"}), 400
    address_service.add_address(data)
    return jsonify(),200

    
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
    return jsonify({"error": "NO addresses found with this CP !"}), 404

#Searching by Municipio will return all of the same Municipio
@app.route('/Mnpio/<Municipio_to_search>', methods=['GET'])
def search_by_estado(Municipio_to_search):
    response = address_service.search_by_Municipio(Municipio_to_search)
    if response: 
        return jsonify(response), 200
    return jsonify({"error": "No Municipalities found"}), 404




if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
