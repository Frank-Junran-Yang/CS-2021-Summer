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
    favorite=db.Column(db.String(1000),unique=True)

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


def digit(p):
    digits='1234567890'
    for digit in digits:
        for i in p:
            if i==digit:
                return True
    return False

def char(p):
    chars='abcdefghijklmnopqrstuvwxyz'
    for char in chars:
        for i in p:
            if i==char:
                return True
    return False

def capital(p):
    capitals='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for capital in capitals:
        for i in p:
            if i==capital:
                return True
    return False


def onetype(name):
    publics=PublicSchools.query.all()
    boardings=BoardingSchools.query.all()
    privates=PrivateSchools.query.all()
    for public in publics:
        if name==public.name:
            return 'publicschool'
    for boarding in boardings:
        if name==boarding.name:
            return 'boardingschool'
    for private in privates:
        if name==private.name:
            return 'privateschool'


def alltype(name):
    publics=PublicSchools.query.all()
    boardings=BoardingSchools.query.all()
    privates=PrivateSchools.query.all()
    type=[]
    for public in publics:
        if name==public.name:
            type.append('publicschool')
    for boarding in boardings:
        if name==boarding.name:
            type.append('boardingschool')
    for private in privates:
        if name==private.name:
            type.append('privateschool')
    return type

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
        str1 += ','

    return str1 


@app.route('/',methods=['POST','GET'])

def index():
    privates= PrivateSchools.query.all()
    publics= PublicSchools.query.all()
    boardings= BoardingSchools.query.all()
    prilen=len(privates)
    publen=len(publics)
    boalen=len(boardings)
    return render_template('index.jinja',privates=privates,publics=publics,boardings=boardings, prilen=prilen, publen=publen, boalen=boalen)

@app.route('/register',methods=['POST','GET'])
def register():
    warning=''
    success=''
    try:
        if (request.method == 'POST'):
            username=request.form.get('username')
            password = request.form.get('password')
            check=request.form.get('check')
            firstname=request.form.get('firstname')
            lastname=request.form.get('lastname')
            if password!=check:
                warning='Password Does Not Match!!!'
                return render_template('register.jinja',warning=warning)

            
            if password==check:
                if len(password)<=6:
                    warning='Your password is too short, please make it longer than 6 characters'
                    return render_template('register.jinja',warning=warning)
                elif len(password)>=20:
                    warning='Your password is too long, please make it no longer than 20 characters'
                    return render_template('register.jinja',warning=warning)
                elif not capital(password):
                    print('no capital')
                    warning='You need to have at least one digit, one capital letter, and one letter'
                    return render_template('register.jinja',warning=warning)
                elif not digit(password):
                    print('no digit')
                    warning='You need to have at least one digit, one capital letter, and one letter'
                    return render_template('register.jinja',warning=warning)
                elif not char(password):
                    print('no letter')
                    warning='You need to have at least one digit, one capital letter, and one letter'
                    return render_template('register.jinja',warning=warning)
                user=User(username=username, password=password, firstname=firstname, lastname=lastname, money=1000)
                db.session.add(user)
                db.session.commit()
                success='Register Successfully'
                print(success)
                return redirect(url_for('login'))
    except:
        return redirect(url_for('register'))
    return render_template('register.jinja',warning=warning,success=success)

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

@app.route('/private/<schoolname>',methods=['POST','GET'])
def privateschool(schoolname):
    school=PrivateSchools.query.filter_by(name=schoolname ).first()
    name=school.name
    location=school.location
    tuitionfee=school.tuitionfee
    rank=school.rank
    size=school.size
    matriculation=school.matriculation
    already=''
    allrank=[]
    type=alltype(name)
    if len(type)>1:
        boardings=BoardingSchools.query.all()
        publics=PublicSchools.query.all()

        for boarding in boardings:
            if name==boarding.name:
                allrank.append(['Boarding Rank',boarding.rank])
        
        for public in publics:
            if name==public.name:
                allrank.append(['Public Rank',public.rank])
        
        allrank.append(['Private Rank',rank])
    else:
        allrank.append(['Private Rank',rank])
    if (request.method=='POST'):
        if request.form.get('add'):
            print('works')
            username=session.get('user')[0]
            user=User.query.filter_by(username=username ).first()
            # print(type(user.favorite))
            # print(str(user.favorite))
            # user.favorite=None
            if str(user.favorite)=='None':
                user.favorite=name
                user.favorite+=','
                # print('The First Round')
            else:
                hello=str(user.favorite).split(',')
                for thing in hello:
                    if name == thing:
                        # print(str(user.favorite))
                        already='This school is already in your favorite!'
                        return render_template('school.jinja',name=name,location=location,tuitionfee=tuitionfee,rank=rank,matriculation=matriculation,size=size, already=already, allrank=allrank)

                user.favorite=str(user.favorite)+name
                user.favorite+=','
                # print('The Normal Round')
            
            # print(str(user.favorite))
            db.session.commit()
    


    return render_template('school.jinja',name=name,location=location,tuitionfee=tuitionfee,rank=rank,matriculation=matriculation,size=size, already=already, allrank=allrank)

@app.route('/public/<schoolname>',methods=['POST','GET'])
def publicschool(schoolname):
    school=PublicSchools.query.filter_by(name=schoolname ).first()
    name=school.name
    location=school.location
    tuitionfee=school.tuitionfee
    rank=school.rank
    size=school.size
    matriculation=school.matriculation
    already=''
    allrank=[]
    type=alltype(name)
    if len(type)>1:
        boardings=BoardingSchools.query.all()
        privates=PrivateSchools.query.all()

        for boarding in boardings:
            if name==boarding.name:
                allrank.append(['Boarding Rank',boarding.rank])
        
        for private in privates:
            if name==private.name:
                allrank.append(['Private Rank',private.rank])
        
        allrank.append(['Public Rank',rank])
    else:
        allrank.append(['Public Rank',rank])

    if (request.method=='POST'):
        if request.form.get('add'):
            print('works')
            username=session.get('user')[0]
            user=User.query.filter_by(username=username ).first()
            # print(type(user.favorite))
            # print(str(user.favorite))
            # user.favorite=None
            if str(user.favorite)=='None':
                user.favorite=name
                user.favorite+=','
                # print('The First Round')
            else:
                hello=str(user.favorite).split(',')
                for thing in hello:
                    if name == thing:
                        # print(str(user.favorite))
                        already='This school is already in your favorite!'
                        return render_template('school.jinja',name=name,location=location,tuitionfee=tuitionfee,rank=rank,matriculation=matriculation,size=size, already=already, allrank=allrank)

                user.favorite=str(user.favorite)+name
                user.favorite+=','
                # print('The Normal Round')
            
            # print(str(user.favorite))
            db.session.commit()

    return render_template('school.jinja',name=name,location=location,tuitionfee=tuitionfee,rank=rank,matriculation=matriculation,size=size, already=already, allrank=allrank)

@app.route('/boarding/<schoolname>',methods=['POST','GET'])
def boardingschool(schoolname):

    school=BoardingSchools.query.filter_by(name=schoolname ).first()
    name=school.name
    location=school.location
    tuitionfee=school.tuitionfee
    rank=school.rank
    size=school.size
    matriculation=school.matriculation
    already=False
    allrank=[]
    type=alltype(name)
    if len(type)>1:
        privates=PrivateSchools.query.all()
        publics=PublicSchools.query.all()

        for private in privates:
            if name==private.name:
                allrank.append(['Private Rank',private.rank])
        
        for public in publics:
            if name==public.name:
                allrank.append(['Public Rank',public.rank])
        
        allrank.append(['Boarding Rank',rank])
    else:
        allrank.append(['Boarding Rank',rank])
    
    username=session.get('user')[0]
    user=User.query.filter_by(username=username ).first()
    hello=str(user.favorite).split(',')
    print(hello)
    print(name)
    for thing in hello:
        if name == thing:
            print('Exist')
            already=True
            if (request.method=='POST'):
                if request.form.get('remove'):
                    print(hello)
                    print(len(hello))
                    hello.remove(name)
                    print(hello)
                    print(len(hello))
                    user.favorite=listToString(hello)
                    print(user.favorite)
                    db.session.commit()
            return render_template('school.jinja',name=name,location=location,tuitionfee=tuitionfee,rank=rank,matriculation=matriculation,size=size, already=already, allrank=allrank)

    print('Not exist')
    if (request.method=='POST'):
        if request.form.get('add'):
            print('works')
            # print(type(user.favorite))
            # print(str(user.favorite))
            # user.favorite=None
            if str(user.favorite)=='None':
                user.favorite=name
                user.favorite+=','
                # print('The First Round')
            else:

                user.favorite=str(user.favorite)+name
                user.favorite+=','
                # print('The Normal Round')
            
            # print(str(user.favorite))
            db.session.commit()
    return render_template('school.jinja',name=name,location=location,tuitionfee=tuitionfee,rank=rank,matriculation=matriculation,size=size, already=already, allrank=allrank)


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
    
    name=session.get('user')[0]
    user=User.query.filter_by(username=name ).first()
    favorite=str(user.favorite)
    hello=favorite.split(',')[:-1]
    print(hello)
    print(len(hello))
    schools=[]
    if len(hello)==0:
        schools.append(['profile',''])
        print('back to profile')
        return render_template('profile.jinja',favorite=favorite,hello=hello,schools=schools)
    for thing in hello:
        schools.append([thing,onetype(thing)])

    # print(hello)
    # print(schools)
    
    return render_template('profile.jinja',favorite=favorite,hello=hello,schools=schools)


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


