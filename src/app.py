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


@app.route("/")
def index():
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
            user.set(username)

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

if __name__ == "__main__":
    app.run(debug=True)