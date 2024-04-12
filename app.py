from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' 

@app.route('/')
def hello():
    # Renderiza a página hello.html
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # processar os dados do formulário.
        # imprimir os dados no console.
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(f"Username: {username}, Email: {email}, Password: {password}")
        
        # Definindo a chave 'username' na sessão
        session['username'] = username
        
        # Redirecionando para a página de boas-vindas após o login bem-sucedido
        return redirect(url_for('welcome'))
    else:
        # Renderiza a página de login quando acessada via GET
        return render_template('login.html')

@app.route('/welcome')
def welcome():
    # Verificando se 'username' existe na sessão
    if 'username' in session:
        return f'Parabéns, seja bem-vindo {session["username"]}. Você fez o login com sucesso!'
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
