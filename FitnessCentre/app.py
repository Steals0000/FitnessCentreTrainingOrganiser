from flask import render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

import models
from database_config import db, app
from login import LoginForm
from signup import RegisterForm
from add import AddForm
from edit import EditForm

bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))


@app.route('/')
def index():
    db.create_all()
    data = models.Date.query.all()
    return render_template('index.html', dates=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('home'))
        return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = models.User(username=form.username.data, name=form.name.data, surname=form.surname.data, midname=form.midname.data, user_lvl=3, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)


@app.route('/home')
@login_required
def home():
    data = models.Date.query.all()
    newdata = data[0]
    return render_template('home.html', FIO=current_user.name+' '+current_user.midname, username=current_user.username, name=current_user.name, surname=current_user.surname, midname=current_user.midname, curdate=newdata, user_lvl=current_user.user_lvl, dates = data)

@app.route('/profile')
@login_required
def profile():
    data = models.Date.query.all()
    return render_template('profile.html', username=current_user.username, name=current_user.name, surname=current_user.surname, midname=current_user.midname, enddate=current_user.enddate, ticket=current_user.ticket, user_lvl=current_user.user_lvl)

@app.route('/daytime')
@login_required
def daytime():
    data = models.Date.query.all()
    data1 = []
    data2 = []
    data3 = []
    data4 = []

    for i in range(6):
        data1.append(data[i])
        data2.append(data[i+6])
        data3.append(data[i + 12])
    for i in range(3):
        data4.append(data[i+18])

    return render_template('daytime.html', id=current_user.id, name=current_user.username, data1=data1, data2=data2, data3=data3, data4=data4, access = 0)

@app.route('/daytime_data/<index>/', methods=['POST'])
@login_required
def daytime_process(index):
    data = models.Date.query.all()
    data1 = []
    data2 = []
    data3 = []
    data4 = []

    for i in range(6):
        data1.append(data[i])
        data2.append(data[i+6])
        data3.append(data[i + 12])
    for i in range(3):
        data4.append(data[i+18])

    date = db.session.query(models.Date).get(index)
    date.users_id.append(current_user)
    date.people_count+=1
    db.session.add(date)
    db.session.commit()
    return render_template('daytime.html', id=current_user.id, name=current_user.username, data1=data1, data2=data2, data3=data3, data4=data4)

@app.route('/admin/del<index>/', methods=['POST'])
@login_required
def admin_del(index):
    user = db.session.query(models.User).get(index)
    db.session.delete(user)
    db.session.commit()
    users = models.User.query.all()
    return render_template('admin.html', id=current_user.id, name=current_user.username, users=users)

@app.route('/admin')
@login_required
def admin():
    users = models.User.query.all()
    clients1 = []
    clients2 = []
    treners = []
    for user in users:
        if user.user_lvl==3:
            clients1.append(user)
        elif user.user_lvl==2:
            clients2.append(user)
        elif user.user_lvl == 1:
            treners.append(user)

    return render_template('admin.html', name=current_user.username, clients1=clients1, clients2=clients2, treners=treners)

@app.route('/admin/edt<index>/', methods=['GET', 'POST'])
@login_required
def edit_frst(index):
    user = db.session.query(models.User).get(index)
    form = EditForm()

    form.name.data = user.name
    form.surname.data = user.surname
    form.midname.data = user.midname
    form.username.data = user.username
    form.ticket.data = user.ticket
    form.enddate.data = user.enddate
    form.lvl.data = user.user_lvl
    return render_template('edit.html', form=form, id=index)

@app.route('/edted<index>', methods=['GET', 'POST'])
@login_required
def edit_scnd(index):
    form = EditForm()
    if form.validate_on_submit():
        user = db.session.query(models.User).get(index)
        user.name = form.name.data
        user.midname = form.midname.data
        user.surname = form.surname.data
        user.username = form.username.data
        user.ticket = form.ticket.data
        user.enddate = form.enddate.data
        user.user_lvl = form.lvl.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('edit.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = models.User(username=form.username.data, name=form.name.data, surname=form.surname.data, midname=form.midname.data, user_lvl=3, password=hashed_password,ticket=form.ticket.data,enddate=form.enddate.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('add.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
