from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return 'User: {} (Email: {})'.format(self.username, self.email)
    def __str__(self):
        return 'User: {} (Email: {})'.format(self.username, self.email)










@app.route('/add/user/<username>/<email>')
def add_user(username, email):
    # ADD OBJECT TO THE DATABASE!!!!
    user = User(username = username, email = email)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('users'))

@app.route('/users')
def users():
    # GET ALL OBJECT FROM USER DATABASE
    users = User.query.all()
    return render_template('users.jinja', users = users)

@app.route('/users/<email>')
def users_email(email):
    users = User.query.filter_by(email = email)
    return render_template('users.jinja', users = users)

if __name__ == '__main__':
    # db.create_all() # TODO: Delete after first time use
    app.run()