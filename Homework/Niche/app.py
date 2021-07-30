from os import readlink
from flask import Flask, render_template, request, redirect, url_for, session
import csv
import random
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'dfghjiouhgyfvhbjaknsdasidnasiodn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///School.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    username = db.Column(db.String(80),unique=True, nullable=True)
    password=db.Column(db.String(80), nullable=True)
    firstname=db.Column(db.String(80), nullable=True)
    lastname=db.Column(db.String(80), nullable=True)
    money=db.Column(db.Integer, nullable=True)
    favorite=db.Column(db.String(1000))

class PrivateSchools(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(80),unique=True, nullable=True)
    location=db.Column(db.String(80), nullable=True)
    tuitionfee=db.Column(db.Integer, nullable=True)
    size=db.Column(db.String(80), nullable=True)
    matriculation=db.Column(db.String(100), nullable=True)
    rank = db.Column(db.Integer, nullable=True)

class PublicSchools(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(80),unique=True, nullable=True)
    location=db.Column(db.String(80), nullable=True)
    tuitionfee=db.Column(db.Integer, nullable=True)
    size=db.Column(db.String(80), nullable=True)
    matriculation=db.Column(db.String(100), nullable=True)
    rank = db.Column(db.Integer, nullable=True)

class BoardingSchools(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(80),unique=True, nullable=True)
    location=db.Column(db.String(80), nullable=True)
    tuitionfee=db.Column(db.Integer, nullable=True)
    size=db.Column(db.String(80), nullable=True)
    matriculation=db.Column(db.String(100), nullable=True)
    rank = db.Column(db.Integer, nullable=True)

@app.route('/',methods=['POST','GET'])

def index():
    privates= PrivateSchools.query.all()
    publics= PublicSchools.query.all()
    boardings= BoardingSchools.query.all()
    return render_template('index.jinja',privates=privates,publics=publics,boardings=boardings)

@app.route('/register',methods=['POST','GET'])
def register():
    try:
        if (request.method == 'POST'):
            username=request.form.get('username')
            password = request.form.get('password')
            check=request.form.get('check')
            firstname=request.form.get('firstname')
            lastname=request.form.get('lastname')
            
            if password!=check:
                return redirect(url_for('register'))
            
            if password==check:
                user=User(username=username, password=password, firstname=firstname, lastname=lastname, money=1000)
                db.session.add(user)
                db.session.commit()

                return redirect(url_for('users'))
    except:
        return redirect(url_for('register'))
    return render_template('register.jinja')

@app.route('/registerprivate',methods=['POST','GET'])
def registerprivate():
    try:
        if (request.method == 'POST'):
            name=request.form.get('name')
            location = request.form.get('location')
            tuitionfee=request.form.get('tuitionfee')
            size=request.form.get('size')
            matriculation=request.form.get('matriculation')
            rank=request.form.get('rank')
            
            private=PrivateSchools(name=name, location=location, tuitionfee=int(tuitionfee), size=size, matriculation=matriculation, rank=int(rank))
            db.session.add(private)
            db.session.commit()

            return redirect(url_for('private.jinja'))
    except:
        return redirect(url_for('registerprivate'))
    return render_template('registerprivate.jinja')


@app.route('/registerpublic',methods=['POST','GET'])
def registerpublic():
    try:
        if (request.method == 'POST'):
            name=request.form.get('name')
            location = request.form.get('location')
            tuitionfee=request.form.get('tuitionfee')
            size=request.form.get('size')
            matriculation=request.form.get('matriculation')
            rank=request.form.get('rank')
            
            public=PublicSchools(name=name, location=location, tuitionfee=int(tuitionfee), size=size, matriculation=matriculation, rank=int(rank))
            db.session.add(public)
            db.session.commit()

            return redirect(url_for('public.jinja'))
    except:
        return redirect(url_for('registerpublic'))
    return render_template('registerpublic.jinja')

@app.route('/registerboarding',methods=['POST','GET'])
def registerboarding():
    try:
        if (request.method == 'POST'):
            name=request.form.get('name')
            location = request.form.get('location')
            tuitionfee=request.form.get('tuitionfee')
            size=request.form.get('size')
            matriculation=request.form.get('matriculation')
            rank=request.form.get('rank')
            
            boarding=BoardingSchools(name=name, location=location, tuitionfee=int(tuitionfee), size=size, matriculation=matriculation, rank=int(rank))
            db.session.add(boarding)
            db.session.commit()

            return redirect(url_for('boarding.jinja'))
    except:
        return redirect(url_for('registerboarding'))
    return render_template('registerboarding.jinja')

@app.route('/users')
def users():
    if (not session.get('user')):
        return redirect(url_for('index'))

    users= User.query.all()
    return render_template('users.jinja', users=users)

@app.route('/private/<schoolname>')
def privateschool(schoolname):
    school=PrivateSchools.query.filter_by(name=schoolname ).first()
    name=school.name
    location=school.location
    tuitionfee=school.tuitionfee
    rank=school.rank
    size=school.size
    matriculation=school.matriculation
    # publicr=0
    # boardingr=0
    # publics=PublicSchools.query.all()
    # boardings=BoardingSchools.query.all()
    # for public in publics:
    #     if public.name==name:
    #         publicr=public.rank
    
    # for boarding in boardings:
    #     if boarding.name==name:
    #         boardingr=boarding.rank
    # if publicr>=0:
    #     publicrank=publicr
    # else:
    #     publicrank=None
    
    # if boardingr>=0:
    #     boardingrank=boardingr
    # else:
    #     boardingrank=None
    # print(publicrank)
    # print(boardingrank)
    
    


    return render_template('school.jinja',name=name,location=location,tuitionfee=tuitionfee,rank=rank,matriculation=matriculation,size=size)

@app.route('/public/<schoolname>')
def publicschool(schoolname):
    school=PublicSchools.query.filter_by(name=schoolname ).first()
    name=school.name
    location=school.location
    tuitionfee=school.tuitionfee
    rank=school.rank
    size=school.size
    matriculation=school.matriculation
    return render_template('school.jinja',name=name,location=location,tuitionfee=tuitionfee,rank=rank,matriculation=matriculation,size=size)

@app.route('/boarding/<schoolname>')
def boardingschool(schoolname):
    school=BoardingSchools.query.filter_by(name=schoolname ).first()
    name=school.name
    location=school.location
    tuitionfee=school.tuitionfee
    rank=school.rank
    size=school.size
    matriculation=school.matriculation
    return render_template('school.jinja',name=name,location=location,tuitionfee=tuitionfee,rank=rank,matriculation=matriculation,size=size)


@app.route('/private')
def private():
    privateschools=[]
    number=[]
    privates= PrivateSchools.query.all()
    for private in privates:
        number.append(private.rank)
    sorted(number)

    for number in sorted(number):
        print(number)
        for private in privates:
            print(private.rank)
            if number==private.rank:
                privateschools.append([private.name,private.rank])
    


    return render_template('private.jinja', privates=privates,privateschools=privateschools)

@app.route('/public')
def public():
    publicschools=[]
    number=[]
    publics= PublicSchools.query.all()
    for public in publics:
        number.append(public.rank)
    sorted(number)

    for number in sorted(number):
        print(number)
        for public in publics:
            print(public.rank)
            if number==public.rank:
                publicschools.append([public.name,public.rank])
    return render_template('public.jinja', publics=publics,publicschools=publicschools)

@app.route('/boarding')
def boarding():

    boardingschools=[]
    number=[]
    boardings= BoardingSchools.query.all()
    for boarding in boardings:
        number.append(boarding.rank)
    sorted(number)

    for number in sorted(number):
        print(number)
        for boarding in boardings:
            print(boarding.rank)
            if number==boarding.rank:
                boardingschools.append([boarding.name,boarding.rank])
    return render_template('boarding.jinja', boardings=boardings,boardingschools=boardingschools)


@app.route('/login',methods=['POST','GET'])
def login():
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        users=User.query.all()
        for user in users:
            print (user.username)
            print (user.password)
            if username==user.username:
                if password==user.password:
                    session['user'] = [user.username, user.password, user.firstname, user.lastname, user.money]
                    return redirect (url_for('index'))

    return render_template('login.jinja')
            

@app.route('/profile',methods=['POST','GET'])

def profile():
    if (not session.get('user')):
        return redirect(url_for('index'))
    
    user=session.get('user')[0]
    return render_template('profile.jinja')


@app.route('/money',methods=['POST','GET'])

def money():
    if (not session.get('user')):
        return redirect(url_for('index'))
    name=session.get('user')[0]
    user=User.query.filter_by(username=name ).first()

    print(name)
    print(user)
    money=user.money

    if (request.method=='POST'):

        if request.form.get('depositbutton'):
            try:
                print('Depositing')
                deposit = int(request.form.get('deposit'))
                if deposit<0:
                    return redirect(url_for('money'))
                user.money += deposit
                db.session.commit()
                return redirect(url_for('money'))
            except:
                return redirect(url_for('money'))

        if request.form.get('withdrawbutton'):
            try:
                print('Withdrawing')
                withdraw = int(request.form.get('withdraw'))
                if withdraw<0:
                    return redirect(url_for('money'))
                user.money -= withdraw
                db.session.commit()
                return redirect(url_for('money'))
            except:
                return redirect(url_for('money'))
            
    return render_template('money.jinja', user=user, money=money)



@app.route('/logout')
def logout():
    if (not session.get('user')):
        return redirect(url_for('index'))
    session['user'] = None
    return redirect(url_for('index'))



if __name__ == "__main__":
    db.create_all()
    app.run()


