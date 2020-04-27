from flask import render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
import models
from database_config import db, app
from login import LoginForm
from signup import RegisterForm

bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        users = models.User.query.filter_by(username=form.username.data).first()
        if users:
            if check_password_hash(users.password, form.password.data):
                login_user(users, remember=form.remember.data)
                return redirect(url_for('home'))
        return '<h1>Неправильное имя или пароль</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = models.User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.create_all()
        db.session.add(new_user)
        db.session.commit()
        return '<h1>Новый пользователь создан!</h1>'
    return render_template('signup.html', form=form)

@app.route('/home')
@login_required
def home():
    return render_template('home.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
