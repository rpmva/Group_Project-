## Information about our project

* We will be exploring the planets in the Milky Way throughout this project.

* You will be able to find information about the planets on our webpage.

* If you want to find out why Pluto is no longer a planet, check it out.

Our project is found here: https://github.com/rpmva/Group_Project-

Markdown of our database table:

| Planet ID | Planet   | # of Moons | Description                                                                                                                                                                                                          |
|-----------|----------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1         | Mercury  | 2          | smallest and innermost planet in the Solar System. Its orbital period around the Sun of 88 days is the shortest of all the planets in the Solar System                                                               |
| 2         | Venus    | 2          | second planet from the Sun, orbiting it every 224.7 Earth days.[12] It has the longest rotation period (243 days) of any planet in the Solar System and rotates in the opposite direction to most other planets.     |
| 3         | Earth    | 1          | third planet from the Sun and the only object in the Universe known to harbor life.                                                                                                                                  |
| 4         | Mars     | 2          | fourth planet from the Sun and the second-smallest planet in the Solar System after Mercury.                                                                                                                         |
| 5         | Jupiter  | 67         | fifth planet from the Sun and the largest in the Solar System. It is a giant planet with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. |
| 6         | Saturn   | 62         | sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius about nine times that of Earth.                                                        |
| 7         | Uranus   | 27         | seventh planet from the Sun. It has the third-largest planetary radius and fourth-largest planetary mass in the Solar System.                                                                                        |
| 8         | Neptune  | 13         | eighth and farthest known planet from the Sun in the Solar System. In the Solar System, it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet.                    |

**Setup Instructions:**

*Make sure to use Python version 2.7.x.*

1. Install virtualenv if needed.

2. If you do not have a virtual environment yet on the project folder, set it up with:
$ virtualenv venv

3. Then activate the virtual environment
$ source venv/bin/activate

4. Install packages
$ pip install -r requirements.txt

5. To initialize the database:
$ python manage.py deploy

6. To run the development server (use -d to enable debugger and reloader):
$ python manage.py runserver -d
