from flask_script import Manager
from group_project import app, db, Planet

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    p1 = Planet(planet='Mercury', moon_number = 2, description = 'smallest and innermost planet in the Solar System. Its orbital period around the Sun of 88 days is the shortest of all the planets in the Solar System.')
    p2 = Planet(planet='Venus', moon_number = 2, description = 'second planet from the Sun, orbiting it every 224.7 Earth days.[12] It has the longest rotation period (243 days) of any planet in the Solar System and rotates in the opposite direction to most other planets.')
    p3 = Planet(planet='Earth', moon_number = 1, description = 'third planet from the Sun and the only object in the Universe known to harbor life. ')
    p4 = Planet(planet='Mars', moon_number = 2, description = 'fourth planet from the Sun and the second-smallest planet in the Solar System after Mercury.')
    p5 = Planet(planet='Jupiter', moon_number = 67, description = 'fifth planet from the Sun and the largest in the Solar System. It is a giant planet with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. ')
    p6 = Planet(planet='Saturn', moon_number = 62, description = 'sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius about nine times that of Earth.')
    p7 = Planet(planet='Uranus', moon_number = 27, description = 'seventh planet from the Sun. It has the third-largest planetary radius and fourth-largest planetary mass in the Solar System.')
    p8 = Planet(planet='Neptune', moon_number = 13, description = 'eighth and farthest known planet from the Sun in the Solar System. In the Solar System, it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet.')
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.add(p6)
    db.session.add(p7)
    db.session.add(p8)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
