from src.api.index import app, task_queue
from flask_cors import CORS


from threading import Thread

import time



def worker():
    while True:
        task = task_queue.get()
        if task is None:
            break
        # Extrai a função e seus argumentos da tarefa
        func, args, kwargs = task['func'], task.get('args', ()), task.get('kwargs', {})
        print("Iniciando exclusão...")
        # Executa a função com os argumentos fornecidos
        response = func(*args, **kwargs)
        print(response)
        task_queue.task_done()

# Executa a aplicação
if __name__ == '__main__':
    # Inicia a thread do worker
    Thread(target=worker, daemon=True).start()
    CORS(app)
    app.run(debug=True, host='0.0.0.0', port=5000)