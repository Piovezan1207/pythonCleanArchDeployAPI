from src.api.index import app, task_queue_delete
from src.external.AplicationExternal import task_queue_deploy
from flask_cors import CORS


from threading import Thread

import time

def deleteWorker():
    while True:
        task = task_queue_delete.get()
        if task is None:
            break
        # Extrai a função e seus argumentos da tarefa
        func, args, kwargs = task['func'], task.get('args', ()), task.get('kwargs', {})
        print("Iniciando exclusão...")
        # Executa a função com os argumentos fornecidos
        response = func(*args, **kwargs)
        print(response)
        task_queue_delete.task_done()

def deployWorker():
    while True:
        task = task_queue_deploy.get()
        if task is None:
            break
        # Extrai a função e seus argumentos da tarefa
        func, args, kwargs = task['func'], task.get('args', ()), task.get('kwargs', {})
        print("Iniciando deploy...")
        # Executa a função com os argumentos fornecidos
        response = func(*args, **kwargs)
        print(response)
        task_queue_deploy.task_done()

# Executa a aplicação
if __name__ == '__main__':
    # Inicia a thread do worker
    Thread(target=deleteWorker, daemon=True).start()
    # Thread(target=deployWorker, daemon=True).start() #Descomentar para fila de deploys
    CORS(app)
    app.run(debug=True, host='0.0.0.0', port=5000)