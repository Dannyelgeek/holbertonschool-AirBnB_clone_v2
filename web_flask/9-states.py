#!/usr/bin/python3
''' starts a Flask web application'''
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


app.route('/states', strict_slashes=False)
def states():
    """ /states path """
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=False)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ /states/<id> path """
    states = storage.all(State)
    for state in states.values():
        if state.id == str(id):
            return render_template('9-states.html', states=state)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db(exception):
    '''remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
