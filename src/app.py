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
    print(current_user.burrice_de_godofredo)

    if request.method == "POST":
        action = request.form.get("action")

        if action == "create":
            title = request.form.get("title")
            title = title if title else "Novo Diário" # se título for "" dai vai o DEFAULT

            diary_id = addDiary(user=current_user, title=title)

            return redirect(url_for('diary', diary_id=diary_id))
        
        elif action == "delete":
            diary_id = int(request.form.get("diary_id"))

            deleteDiary(diary_id)


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
        title = request.form.get('title')
        content = request.form.get('content')
        share = request.form.get('share')

        updateDiary(id=diary_id, title=title, content=content, share=share)
        
        return redirect(url_for('index'))
        

    # Obter o diário
    diary = getDiary(diary_id)

    # Verificar se o diário existe
    if not diary:
        flash("Diário não encontrado", "error")
        return redirect(url_for("index"))

    # Verificar se o diário é privado (share = false) e o usuário não é o dono
    if not diary['dia_share'] and diary['dia_usu_id'] != current_user.id:
        flash("Você não tem permissão para acessar este diário.", "error")
        return redirect(url_for("index"))

    return render_template("diario.html", diary=diary)


@app.route("/profile/<int:user_id>")
def profile(user_id):
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)