from flask import Flask, redirect, url_for, render_template, flash, request
from forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY']='a43a3d1d4042a1a2291284552fd3f8ee'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///save.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

class User(db.Model, UserMixin):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/home", methods=["GET","POST"])
@login_required
def home():
    return render_template("home.html",title="Home Page")

@app.route("/logout")
def logout():
    logout_user()
    flash('Logged Out !' , 'warning')
    return redirect(url_for('login'))

@app.route("/login")
@app.route("/", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():   
        user = User.query.filter_by(username=form.username.data).first()
        pwd = user.password
        if (user) and (pwd == form.password.data): 
            login_user(user)
            next_page = request.args.get('next')
            flash(f'Logged in as {form.username.data} !' , 'success')
            return redirect(next_page) if next_page else redirect(url_for('login'))
            # return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful' , 'danger')
    return render_template("login.html",title="Login Page" , form =form)



if __name__=="__main__":
    app.run(debug=True)