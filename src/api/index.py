from ..controllers.Application import Application
from ..external.Aplication import NoderedAzure
from ..external.Reservation import GacReservations

from flask import Flask, jsonify, request

# Cria a aplicação Flask
app = Flask(__name__)

@app.route('/nodered', methods=['GET'])
def createNodered():
    reservationId = request.args["id"]

    nodeRedAzure = NoderedAzure()
    gacReservations = GacReservations()
    response = Application.instantiate(reservationId, "Nodered", nodeRedAzure, gacReservations)
    return jsonify(response)

@app.route('/nodered', methods=['DELETE'])
def deleteNodered():
    applicationId = request.args["id"]
    response = Application.delete(applicationId, NoderedAzure)
    return jsonify(response)

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
