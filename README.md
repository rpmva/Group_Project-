## Information about our project

We will be exploring the planets in the Milky Way throughout this project.

You will be able to find information about the planets on our webpage.

If you want to find out why Pluto is no longer a planet, check it out.

Our project is found here: https://github.com/rpmva/Group_Project- 

Setup Instructions:

Make sure to use Python version 2.7.x.

Install virtualenv if needed.

If you do not have a virtual environment yet on the project folder, set it up with:

$ virtualenv venv
Then activate the virtual environment

$ source venv/bin/activate
Install packages

$ pip install -r requirements.txt
To initialize the database:

$ python manage.py deploy
To run the development server (use -d to enable debugger and reloader):

$ python manage.py runserver -d
