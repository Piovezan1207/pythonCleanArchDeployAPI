from src.api.index import app

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)