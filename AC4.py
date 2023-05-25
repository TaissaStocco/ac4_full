from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    
    conn = sqlite3.connect('ac04_fulltack.db')
    cursor = conn.cursor()

   
    cursor.execute('SELECT * FROM dados')
    result = cursor.fetchall()

    
    conn.close()

    # Retornar os dados em formato JSON
    return {'data': result}

@app.route('/data', methods=['POST'])
def post_data():
    # Obter os dados enviados na solicitação POST
    data = request.get_json()

    # Conectar ao banco de dados
    conn = sqlite3.connect('ac04_fulltack.db')
    cursor = conn.cursor()

    # Executar a inserção dos dados no banco
    cursor.execute('INSERT INTO dados (coluna1, coluna2) VALUES (?, ?)', (data['valor1'], data['valor2']))

    # Salvar as alterações e fechar a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Retornar uma resposta de sucesso
    return {'message': 'Dados inseridos com sucesso'}

if __name__ == '__main__':
    # Criar a tabela no banco de dados (se não existir)
    conn = sqlite3.connect('ac04_fulltack.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS dados (coluna1 TEXT, coluna2 TEXT)')
    conn.close()

    # Executar o servidor Flask
    app.run()