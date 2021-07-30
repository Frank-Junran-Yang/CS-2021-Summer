from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shelter.db'
db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    species = db.Column(db.String(90))
    color = db.Column(db.String(20))

    def __repr__(self):
        return 'Animal: {}'.format(self.name)
    def __str__(self):
        return 'Animal: {}'.format(self.name)


@app.route('/add', methods = ['POST', 'GET'])
def add():
    if (request.method == 'POST'):
        name = request.form.get('name')
        species = request.form.get('species')
        color = request.form.get('color')

        pet = Pet(name = name, species = species, color = color)
        db.session.add(pet)
        db.session.commit()

        return redirect(url_for('pets'))

    return render_template('add.jinja')

@app.route('/pets')
def pets():
    pets = Pet.query.all()
    return render_template('pets.jinja', pets = pets)
    
@app.route('/pets/name/<name>')
def pets_name(name):
    pets = Pet.query.filter_by(name = name)
    return render_template('pets.jinja', pets = pets)
@app.route('/pets/species/<s>')
def pets_species(s):
    pets = Pet.query.filter_by(species = s)
    return render_template('pets.jinja', pets = pets)

@app.route('/pets/<id>', methods = ['POST', 'GET'])
def pet(id):
    pet = Pet.query.filter_by(id = id).first()

    if (request.method == 'POST'):
        db.session.delete(pet)
        db.session.commit()
        return redirect(url_for('pets'))
    return render_template('pet.jinja', pet = pet)







if __name__ == '__main__':
    db.create_all() # TODO: Delete after first time use
    app.run()