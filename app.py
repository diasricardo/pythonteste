from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash'

usuarios = [
    {"id": 2, "nome": "Maria", "email": "maria@email.com"}
]  # Lista vazia inicialmente

@app.route('/')
def index():
    return render_template('index.html', usuarios=usuarios)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    email = request.form.get('email')

    # Erro proposital: Falta de validação mais rigorosa
    if nome == "" or email == "":
        flash('Preencha todos os campos!')
        return redirect('/')

    # Erro proposital: Não há verificação para e-mails duplicados
    usuarios.append({"nome": nome, "email": email})
    flash('Usuário adicionado com sucesso!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
