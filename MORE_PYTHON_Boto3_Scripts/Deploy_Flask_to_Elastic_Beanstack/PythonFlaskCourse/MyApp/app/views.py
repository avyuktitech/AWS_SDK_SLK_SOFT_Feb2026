from flask import flash,redirect, url_for,request, render_template
from .form import LoginForm
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import UserInfo, Article
from flask_login import login_user, login_required, logout_user

@app.route('/')
#@login_required
def index():
    #name = current_user.username
    articles = Article.query.all()

    return render_template('index.html', articles=articles)


@app.route('/add', methods = ['GET','POST'])
@login_required
def add_article():
    #form = AddForm()

    if request.method == "POST":

        title = request.form['title']
        description = request.form['description']

        new_article = Article(title=title, description=description)

        db.session.add(new_article)
        db.session.commit()
        flash("Article added successfully")
        return redirect(url_for('index'))




@app.route('/update', methods = ['GET', 'POST'])
@login_required
def update():
    if request.method == "POST":
        my_data = Article.query.get(request.form.get('id'))

        my_data.title = request.form['title']
        my_data.description  = request.form['description']

        db.session.commit()
        flash("Article is updated")

        return redirect(url_for('index'))


@app.route('/delete/<id>/', methods = ['GET', 'POST'])
@login_required
def delete(id):
    my_data = Article.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Article is deleted")
    return redirect(url_for('index'))



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = UserInfo.query.filter_by(username = form.username.data).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)

                    return redirect(url_for('index'))
                flash("Invalid credentials")

    return render_template('login.html', form=form)


@app.route('/register', methods =['GET', 'POST'])
def register():

    if request.method == "POST":
        hashed_password = generate_password_hash(request.form['password'], method='sha256')

        username = request.form['username']
        password = hashed_password
        email = request.form['email']

        new_register = UserInfo(username=username, password=password, email=email)

        db.session.add(new_register)
        db.session.commit()
        flash("Registration was successfull")
        return redirect(url_for('login'))





@app.route('/logout')
#@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
