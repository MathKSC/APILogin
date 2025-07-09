🛡️ API de Login com Flask
Esta é uma API simples criada com o framework Flask, que realiza a verificação de login através de uma requisição POST com dados em JSON.

📌 Funcionalidade
A API possui um único endpoint /login que verifica se os dados enviados (usuário e senha) estão corretos. Em caso positivo, retorna uma mensagem de sucesso; caso contrário, informa erro de autenticação.

🚀 Como Executar o Projeto
1. Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina. Você pode instalar o Flask com o seguinte comando:

bash
Copiar código
pip install flask
2. Executando a API
Salve o código em um arquivo, por exemplo: app.py

Em seguida, execute o arquivo:

bash
Copiar código
python app.py
A API ficará disponível em: http://localhost:5000

🔁 Endpoint
/login - Verificar Login
Método: POST

Conteúdo esperado (JSON):

json
Copiar código
{
  "usuario": "Pedro",
  "senha": 1234
}
Respostas:

✅ 200 OK: Login bem-sucedido

❌ 401 Unauthorized: Usuário ou senha inválidos

🧠 Explicação do Código
Flask: framework web usado para criar a API.

request.get_json(): converte a entrada JSON recebida na requisição para um dicionário Python.

O dicionário usuarios armazena credenciais simples (para fins de exemplo).

O endpoint /login faz a verificação do usuário e senha e retorna uma resposta em JSON.
