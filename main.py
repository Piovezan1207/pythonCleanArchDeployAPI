from src.api.index import app
from flask_cors import CORS

# Executa a aplicação
if __name__ == '__main__':
    CORS(app)
    app.run(debug=True, host='0.0.0.0', port=5000)