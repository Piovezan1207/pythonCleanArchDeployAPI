from ..controllers.ApplicationController import ApplicationController
from ..external.AplicationExternal import NoderedAzure
from ..external.ReservationExternal import GacReservations
from ..errors.ApiError import ApiError

from flask import Flask, jsonify, request

from queue import Queue
# Instância única da fila
task_queue_delete = Queue()

# Função auxiliar para adicionar tarefas
def add_task(func, *args, **kwargs):
    task_queue_delete.put({'func': func, 'args': args, 'kwargs': kwargs})

# Cria a aplicação Flask
app = Flask(__name__)

@app.route('/nodered', methods=['GET'])
def createNodered():
    
    
    reservationId = request.args["id"]
    
    # value = {"url" : "www.nodered.hubsenai.com",
    #              "tempToFinish" : 15}
    
    # return jsonify(value)

    nodeRedAzure = NoderedAzure()
    gacReservations = GacReservations()

    # response = Application.instantiate(reservationId, "Nodered", nodeRedAzure, gacReservations)
    # print(response)
    try:
        response = ApplicationController.instantiate(reservationId, "Nodered", nodeRedAzure, gacReservations)
        print(response)
    except ApiError as e:
        return jsonify( value = {"status" : "Error",
                        "message" : str(e) })
    except Exception as e:
        print("Error" , e)
        return jsonify( value = {"status" : "Error",
                        "message" : "Internal server error" }), 500

    return jsonify(response)

@app.route('/nodered/delete', methods=['GET'])
def deleteNodered():
    applicationId = request.args["id"]
    nodeRedAzure = NoderedAzure()
    
    add_task(ApplicationController.delete, applicationId, nodeRedAzure)
    
    # response = Application.delete(applicationId, nodeRedAzure)
    
    response = {
        "delete" : "{} adicionado a fila para ser removido.".format(applicationId)
    }
    
    return jsonify(response)

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
