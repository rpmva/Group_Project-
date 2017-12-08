import os
from flask import Flask, session, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class Planet(db.Model):
     __tablename__ = 'professors'
     id = db.Column(db.Integer, primary_key=True)
     planet = db.Column(db.String(64))
     moon_number = db.Column(db.Integer)
     description = db.Column(db.Text)


@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/planets')
def planets():
      planets = [
      ['Mercury', 2, 'smallest and innermost planet in the Solar System. Its orbital period around the Sun of 88 days is the shortest of all the planets in the Solar System.'],
      ['Venus', 2, 'second planet from the Sun, orbiting it every 224.7 Earth days.[12] It has the longest rotation period (243 days) of any planet in the Solar System and rotates in the opposite direction to most other planets.'],
      ['Earth', 1, 'third planet from the Sun and the only object in the Universe known to harbor life.'],
      ['Mars', 2, 'fourth planet from the Sun and the second-smallest planet in the Solar System after Mercury.'],
      ['Jupiter', 67, 'fifth planet from the Sun and the largest in the Solar System. It is a giant planet with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined.'],
      ['Saturn',  62, 'sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius about nine times that of Earth.'],
      ['Uranus', 27, 'seventh planet from the Sun. It has the third-largest planetary radius and fourth-largest planetary mass in the Solar System.'],
      ['Neptune', 13,  'eighth and farthest known planet from the Sun in the Solar System. In the Solar System, it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet.']
      ]

      return render_template('planets.html', planets=planets)


@app.route('/planets-directory')
def show_all_planets():
    planets =Planet.query.all()
    return render_template('planet-all.html', planets=planets)


@app.route('/planets-directory/edit/<int:id>', methods=['GET', 'POST'])
def edit_planet(id):
    planet = Planet.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('planet-edit.html', planet=planet)
    if request.method == 'POST':
        planet.planet = request.form['planet']
        planet.moon_number = request.form['moon_number']
        planet.description = request.form['description']
        db.session.commit()
        return redirect(url_for('show_all_planets'))


@app.route('/planets-directory/add', methods=['GET', 'POST'])
def add_planets():
    if request.method == 'GET':
       return render_template('planet-add.html')
    if request.method == 'POST':
       planet = request.form['planet']
       moon_number = request.form['moon_number']
       description = request.form['description']

       planet = Planet(planet=planet, moon_number=moon_number, description=description)
       db.session.add(planet)
       db.session.commit()
       return redirect(url_for('show_all_planets'))


@app.route('/planets-directory/delete/<int:id>', methods=['GET', 'POST'])
def delete_planet(id):
    planet = Planet.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('planet-delete.html', planet=planet)
    if request.method == 'POST':
        db.session.delete(planet)
        db.session.commit()
        return redirect(url_for('show_all_planets'))


@app.route('/members')
def about():
    return render_template('members.html')


if __name__ == '__main__':
    app.run()
