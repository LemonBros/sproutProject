import os

#get the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# config object used for Flask application
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "sqlite:///" + os.path.join(basedir, 'app.db')
    
    #disables letting application know
    #everytime a change is made.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
