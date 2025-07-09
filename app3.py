from flask import Flask, request, jsonify

app3 = Flask(__name__) #criando instância

usuarios = {
    'usuario': 'Pedro',
    'senha': 1234,
}

@app3.route('/login', methods = ['POST']) #defini o url especifico que vai direcionar o cliente para o login
def verificacao_login():
    dados = request.get_json() #pega a resposta do cliente e converte de json para python

    usuario = dados.get('usuario') #vão extrair os dados 'usuario' e 'senha' separadamente do json
    senha = dados.get('senha') #deixando mais seguro e organizado

    if usuario in usuarios and usuario[usuario] == senha:
        return jsonify({'mensagem': 'login bem sucedido!'}), 200 #retorna a o usuario em formato json que seu 'login' funcionou

    else: return jsonify({'mensagem': 'usuário ou senha inválidos'}), 401
if __name__ == '__main__':
    app3.run(port=5000, host='localhost', debug=True)
