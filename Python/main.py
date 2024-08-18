#Imports
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
#from flask_scss import Scss

#My app
app = Flask(__name__)
app.secret_key = "your_secret_key"

#Configure SQL Alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATONS"] = False
db = SQLAlchemy(app)

#Database Model
class User(db.Model):
    # Class Variables
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(25), unique=False, nullable = False)
    username = db.Column(db.String(25), unique=True, nullable = False)
    email = db.Column(db.String(50), unique=True, nullable = False)
    password_hash = db.Column(db.String(150), nullable = False)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Routs
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template("index.html")

    
# Login
@app.route("/", methods=["POST"])
def login():
    #collect info from the form
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return render_template("index.html", Warning = 'Please enter correct username and password')

# Register
# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        user = User.query.filter_by(username=username).first()
        email_user = User.query.filter_by(email=email).first()
        parts = email.split('@')
     
        if parts[1] != "gmail.com":
            return render_template('register.html', error3 ='Invalid email')

        if user:
            return render_template('register.html', error ='User already exists')
        if email_user:
            return render_template('register.html', error ='User already exists')
        else:
            if confirm_password == password:
                new_user = User(name=name, username=username, email = email)
                new_user.set_password(password)
                db.session.add(new_user)
                db.session.commit()
                session['username'] = username
                return render_template('register.html', message ='Registration successful')
            else:
                return render_template('register.html', error2 ='Both password are not same')
    else:
        return render_template('register.html')


# Dashboard
@app.route('/dashboard')
def dashboard():
    if "username" in session:
        return render_template('dashboard.html', username = session['username'])
    return redirect(url_for('home')) #if user not there back to home


# Logout 
@app.route('/logout')
def logout():
    session.pop('username', None) # user is session
    return redirect(url_for('home'))

@app.route('/login')
def temp():
    return render_template('index.html')

if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)




  