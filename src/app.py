from flask import *
from aux_funcs.func import *
from werkzeug.security import check_password_hash, generate_password_hash
from database.__init__ import initDatabase

login_manager = LoginManager()

app = Flask(__name__)

login_manager.init_app(app)


app.secret_key = "UDD36D)6+1&4.W5l3I33x^Qivr=gbT[t{r3u#aQ,+/GA<>10J!"


initDatabase()


@login_manager.user_loader
def load_user(user_id): # user_id = email
    return User.get(user_id)


@app.route("/", methods=["GET", "POST"])

def index():
    logged_in = current_user.is_authenticated

    if request.method == "POST":
        action = request.form.get("action")

        if action == "create":
            title = request.form.get("title")
            title = title if title else "Novo Diário" # se título for "" dai vai o DEFALT

            diary = Diary(current_user)
            diary.create(title=title)

        elif action == "delete":
            diary_id = int(request.form.get("diary_id"))

            diary = Diary(current_user)
            diary.delete(diary_id)

        return redirect(url_for("index"))

    # busca os diários do usuário para exibir no HTML
    if logged_in:
        connection = get_connection()
        diaries = connection.execute(
            "SELECT * FROM tb_diarios WHERE dia_usu_id = ? ORDER BY dia_date ASC",
            (current_user.id,)).fetchall()
        connection.close()
        return render_template("index.html", logged_in=logged_in, diaries=diaries)

    return render_template("index.html", logged_in=current_user.is_authenticated)


# Rota de Cadastro
@app.route("/register", methods = ['GET', 'POST'])
def register():
    # Se não tiver um user, será cadastrado. Se tiver um identificador no banco de dados ele será redirecionado para a página de login
    if request.method == 'POST':
        # Coletando dados do formulário
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if not User.get(email): # Se ainda não existir um user com esse email
            password_hash = generate_password_hash(password)

            user = User(email, password_hash)
            user.add(username)

        return redirect(url_for("login"))


    return render_template("register.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    # Se tiver user cadastrado será redirecionado para a Home Page e logado, se não, será avisado que email ou senha estão errados 
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = load_user(email)

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for("index"))

    return render_template("login.html")

@app.route("/logout", methods = ["GET", "POST"])
@login_required
def logout():

    if request.method == "POST":
        logout_user()
        return redirect(url_for('index'))

    return render_template("logout.html")

@app.route("/diario/<int:diary_id>", methods=["GET", "POST"])
@login_required
def diary(diary_id):
    if request.method == "POST":
        ...

    # Busca o diário específico com o id do diário e o id do usuário logado
    connection = get_connection()
    diary = connection.execute(
        "SELECT * FROM tb_diarios WHERE dia_id = ? AND dia_usu_id = ?",
        (diary_id, current_user.id)).fetchone()
    connection.close()

    # Se o diário não existir ou não pertencer ao usuário atual, retorna um erro ou redireciona
    if not diary:
        return 'Você não tem permissão para acessar este diário.', 403

    # Se o diário pertence ao usuário, renderiza a página com o diário
    return render_template("diario.html", diary=diary)



if __name__ == "__main__":
    app.run(debug=True)