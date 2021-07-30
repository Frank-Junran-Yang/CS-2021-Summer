from flask import Flask, render_template
import csv
from user import User

app=Flask(__name__)


@app.route('/users')
def users():
    information=[]
    with open('user.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                user=User(fname=row[0],lname=row[1],email=row[2],password=row[3])
                information.append(user)
    return render_template('users.jinja',information=information)

if __name__ == '__main__':
    app.run()

