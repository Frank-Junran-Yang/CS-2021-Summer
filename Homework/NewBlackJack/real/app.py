from flask import Flask, render_template, request, redirect, url_for, session
import csv
import random
from flask_sqlalchemy import SQLAlchemy
from blackjack import Card, Deck, Player, Game
app = Flask(__name__)
app.secret_key = 'dfghjiouhgyfvhbjaknsdasidnasiodn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    username = db.Column(db.String(80),unique=True, nullable=True)
    password=db.Column(db.String(80), nullable=True)
    firstname=db.Column(db.String(80), nullable=True)
    lastname=db.Column(db.String(80), nullable=True)
    money=db.Column(db.Integer, nullable=True)


@app.route('/',methods=['POST','GET'])

def index():
    hello='Nihao'
    return render_template('index.jinja',hello=hello)

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


@app.route('/users')
def users():
    if (not session.get('user')):
        return redirect(url_for('index'))

    users= User.query.all()
    return render_template('users.jinja', users=users)

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
                    return redirect (url_for('profile'))

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
    # username=session.get('user')[0]
    # password=session.get('user')[1]
    # firstname=session.get('user')[2]
    # lastname=session.get('user')[3]
    # money=int(session.get('user')[4])
    # print(user)
    # print(username)
    # print(password)
    # print(firstname)
    # print(lastname)
    # print(money)
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

                
            
            # try:
            #     deposit = int(request.form.get('deposit'))
            #     user.money += deposit
            #     db.session.commit()
            #     return redirect(url_for('money'))

            # except ValueError:
            #     return redirect(url_for('money'))
            
            try:
                
                if request.form.get('withdraw'):
                    withdraw = int(request.form.get('withdraw'))
                    user.money -= withdraw
                    db.session.commit()
                    return redirect(url_for('money'))
        # nuser=User(username=username, password=password, firstname=firstname, lastname=lastname, money=money)
        # db.session.delete(user)
        # db.session.add(nuser)
            except:
                return redirect(url_for('money'))

            # try:
                
            #     if request.form.get('withdraw'):
            #         withdraw = int(request.form.get('withdraw'))
            #         user.money -= withdraw
            #         db.session.commit()
            #         return redirect(url_for('money'))
            # except ValueError:
            #     return redirect(url_for('money'))
            
    return render_template('money.jinja', user=user, money=money)



@app.route('/logout')
def logout():
    if (not session.get('user')):
        return redirect(url_for('index'))
    session['user'] = None
    return redirect(url_for('index'))
        


        












def getsum(self):
    p=[]
    for row in self:
        if row[0]=='J':
            p.append(10)
        elif row[0]=='Q':
            p.append(10)
        elif row[0]=='K':
            p.append(10)
        elif row[0]=='A':
            p.append(1)
        elif row[0]=='1':
            if row[1]=='0':
                p.append(10)
        else:
            p.append(int(row[0]))
    return sum(p)
        
def deal(self):
    top = self[0]
    self.pop(0)
    with open('cards.csv', 'w',newline='',encoding="utf-8") as file:
        csv_writer = csv.writer(file, delimiter =',')
        csv_writer.writerow(self)
    return top





#     return render_template('add.jinja')
@app.route('/start',methods=['POST','GET'])
def start():
    if (request.method == 'POST'):
        print('begin')
        d=Deck()
        d.shuffle()
        a=d.cards
#         print(type(a))
        print(a)
        session['card']=[[],0]
        with open('cards.csv', 'w',newline='',encoding="utf-8") as file:
            csv_writer = csv.writer(file, delimiter =',')
            csv_writer.writerow(a)
        # print(session.get('cards')[0])


#         #  card.clear()
# #         print(card)
        return redirect(url_for('game'))
        
    return render_template('start.jinja')

@app.route('/game',methods = ['POST', 'GET'])
def game():
    # user=Player('Frank')
    # game=Game(user)
    print('hello')
    result=''
    stop=''
    # d=Deck()
    # d.shuffle()
    # a=d.cards
    # print(type(a))
    # print(a)
    # with open('card.csv', 'w',newline='',encoding="utf-8") as file:
    #     csv_writer = csv.writer(file, delimiter =',')
    #     csv_writer.writerow(a)

    # print(d)
    name=session.get('user')[0]
    user=User.query.filter_by(username=name ).first()
    if user.money<=0:
        result="YOU DON'T HAVE ENOUGH MONEY"
        return redirect(url_for('start'))

    if (request.method == 'POST'):
        if request.form.get('new'):
            if session.get('card')[1]>21:
                return redirect(url_for('game'))
            if session.get('card')[1]<21:
                print('It works')
                data = []
                with open('cards.csv',encoding="utf-8") as file:
                    csv_reader = csv.reader(file, delimiter = ',')
                    for row in csv_reader:
                        data.append(row)
                print(data[0])


                # deck=[]
                # for row in session.get('cards')[0]:
                #     deck.append(row)

                
                card=[]
                card=session.get('card')[0]
                card.append(deal(data[0]))
                print(card)

                # session['cards']=[deck]
                sum=getsum(card)
                session['card']=[card,sum]
                print(session.get('card')[0])
            
            if session.get('card')[1]==21:
                result='You Win 500'
                user.money += 500
                db.session.commit()

            if session.get('card')[1]>21:
                result='You lose 200'
                user.money -=200
                db.session.commit()



        if request.form.get('stop'):
            print('Start again')
            if session.get('card')[1]>21:
                stop='Are you trying to crush the code??????'
                user.money=user.money
            if session.get('card')[1]==21:
                result='You Win 500'
                user.money += 500
                db.session.commit()
            if session.get('card')[1]<21:
                result='You Lose'
                if session.get('card')[1]==20:
                    user.money += 300
                    db.session.commit()
                    result='You win 300'
                if session.get('card')[1]==19:
                    user.money += 200
                    db.session.commit()
                    result='You win 200'
                if session.get('card')[1]==18:
                    user.money +=150
                    db.session.commit()
                    result='You win 150'
                if session.get('card')[1]==17:
                    user.money +=50
                    db.session.commit()
                    result='You win 50'
                if session.get('card')[1]==16:
                    user.money +=10
                    db.session.commit()
                    result='You win 10'
                if session.get('card')[1]==15:
                    user.money -=10
                    db.session.commit()
                    result='You lose 10'
                if session.get('card')[1]==14:
                    user.money -=50
                    db.session.commit()
                    result='You lose 50'
                if session.get('card')[1]==13:
                    user.money -=100
                    db.session.commit()
                    result='You lose 100'
        if request.form.get('restart'):

            return redirect(url_for('start'))
        

        # print(card)
        # print(getsum(card))

        # sumcard=getsum(card)
        # if sumcard>=21:
        #     result='You lose'
            # return redirect(url_for('index'))
        # else:
        #     result='Please continue'

        

        

        

        # session['cards'] = []
    # name='Frank'
    # user=Game(name)
    # if (request.method == 'POST'):
        
    #     choice = request.form.get('Your choice')

    #     if choice=='yes':
    #         ngame= Game(Player(name))
    #         ngame.turn()

    return render_template('game.jinja',result=result,user=user, stop=stop)



if __name__ == "__main__":
    db.create_all()
    app.run()


