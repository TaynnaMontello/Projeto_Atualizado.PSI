from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from database import get_db_connection

app = Flask(__name__)
app.secret_key = "supersecreto123"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'

class User(UserMixin):
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        return User(id=user_data['id'], nome=user_data['nome'], email=user_data['email'])
    return None

@app.route('/')
def index():
    return render_template('index.html', usuario=current_user)

from flask import make_response

@app.route('/lembrar_usuario')
def lembrar_usuario():
    resposta = make_response(redirect(url_for('index')))
    resposta.set_cookie('nome_usuario', current_user.nome)
    return resposta


@app.route('/cadastrar_pessoa', methods=['GET', 'POST'])
def cadastrar_pessoa():
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        email = request.form['email'].strip()
        senha = request.form['senha'].strip()

        if not nome or not email or not senha:
            flash('Preencha todos os campos.')
            return redirect(url_for('cadastrar_pessoa'))

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
        usuario_existente = cursor.fetchone()

        if usuario_existente:
            conn.close()
            flash('Este e-mail já está cadastrado.')
            return redirect(url_for('cadastrar_pessoa'))

        senha_hash = generate_password_hash(senha)

        cursor.execute(
            'INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)',
            (nome, email, senha_hash)
        )
        conn.commit()
        conn.close()

        flash('Usuário registrado com sucesso!')
        return redirect(url_for('login'))

    return render_template('cadastrar_pessoa.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip()
        senha = request.form['senha'].strip()

        if not email or not senha:
            flash('Preencha todos os campos, por favor 💌')
            return redirect(url_for('login'))

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
        usuario = cursor.fetchone()
        conn.close()

        if usuario and check_password_hash(usuario['senha'], senha):
            user = User(id=usuario['id'], nome=usuario['nome'], email=usuario['email'])
            login_user(user)
            flash('Login feito com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('E-mail ou senha incorretos.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/projetos/novo', methods=['GET', 'POST'])
@login_required
def cadastrar_projeto():
    if request.method == 'POST':
        titulo = request.form['titulo'].strip()
        descricao = request.form['descricao'].strip()
        usuario = current_user.nome 

        if not titulo or not descricao:
            flash('Todos os campos devem ser preenchidos.')
            return redirect(url_for('cadastrar_projeto'))

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            'INSERT INTO projetos (titulo, descricao, usuario) VALUES (?, ?, ?)',
            (titulo, descricao, usuario)
        )
        conn.commit()
        conn.close()

        flash('Projeto cadastrado com sucesso!')
        return redirect(url_for('listar_projetos'))

    return render_template('cadastrar_projeto.html')

@app.route('/projetos')
@login_required
def listar_projetos():
    conn = sqlite3.connect('jogo.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT titulo, descricao, usuario FROM projetos ORDER BY id DESC")
    projetos = cursor.fetchall()

    conn.close()
    return render_template('projetos.html', projetos=projetos)

@app.route('/meus-projetos')
@login_required
def meus_projetos():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM projetos WHERE usuario = ?',
        (current_user.nome,)
    )
    projetos = cursor.fetchall()
    conn.close()

    return render_template('meus_projetos.html', projetos=projetos)

@app.route('/editar_projeto/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_projeto(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()

        if titulo and descricao:
            cursor.execute(
                'UPDATE projetos SET titulo = ?, descricao = ? WHERE id = ? AND usuario = ?',
                (titulo, descricao, id, current_user.nome)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('meus_projetos'))
        conn.close()
        return redirect(url_for('editar_projeto', id=id))

    cursor.execute('SELECT * FROM projetos WHERE id = ? AND usuario = ?', (id, current_user.nome))
    projeto = cursor.fetchone()
    conn.close()

    return render_template('editar_projeto.html', projeto=projeto)


@app.route('/excluir_projeto', methods=['POST'])
@login_required
def excluir_projeto():
    projeto_id = request.form.get("id") 
    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM projetos WHERE id = ?", (projeto_id,))
    conn.commit()
    conn.close()

    flash("Projeto excluído com sucesso!")
    return redirect(url_for("meus_projetos"))

@app.route('/sobre')
def sobre():
    return render_template('/sobre.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu com sucesso! 💔')
    return redirect(url_for('login'))

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def erro_interno(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
