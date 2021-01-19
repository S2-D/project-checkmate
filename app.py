from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from login import LoginForm, SignupForm, User, users

#Flask 객체 인스턴스 생성
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'secrtidsfjo222'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  if len(users) == 1:
    return users[0]
  else:
    return users[1]

@app.route('/') # 접속하는 url
def index():
  return render_template('index.html')

  @app.route('/todo_personal') # 접속하는 url
def index():
  return render_template('todo_personal.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  if form.validate_on_submit():
    hashed_pw = generate_password_hash(form.password.data, method='sha256')
    new_user = User(form.username.data, form.email.data, hashed_pw)
    new_user.create_user()
    return redirect(url_for('login'))
  return render_template('signup_tp.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = [x for x in users if x.username == form.username.data][0]
    if user:
      if check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('dashboard'))
      else:
          return "Invalid password"
  return render_template('login_tp.html', form=form)

@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
  return render_template('dash_tp.html', name = current_user.username)

if __name__=="__main__":
  app.run(debug=True)
