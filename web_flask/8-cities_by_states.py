#!/usr/bin/python3
''' starts a Flask web application'''
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def st_ct_list():
    data = {
        'st': storage.all(State).values(),
        'ct': storage.all(City).values()
    }
    return render_template('8-states_list.html', data=data)


@app.teardown_appcontext
def teardown_db(exception):
    '''remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
