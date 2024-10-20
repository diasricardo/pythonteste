from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash'

# Lista para armazenar dados temporariamente
usuarios = [
    {"id": 1, "nome": "João", "email": "joao@email.com"},
    {"id": 2, "nome": "Maria", "email": "maria@email.com"}
]

@app.route('/')
def index():
    return render_template('index.html', usuarios=usuarios)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    email = request.form.get('email')

    if not nome or not email:
        flash('Todos os campos são obrigatórios!')
        return redirect(url_for('index'))

    # Erro proposital: ID gerado incorretamente como string
    novo_usuario = {"id": str(len(usuarios) + 1), "nome": nome, "email": email}
    usuarios.append(novo_usuario)

    flash('Usuário adicionado com sucesso!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
