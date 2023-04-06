#!/usr/bin/python3
''' starts a Flask web application'''
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<path:id>', strict_slashes=False)
def path_st_list(id):
    all_states = storage.all(State)

    if not id:
        return render_template(
            '7-states_list.html',
            items=all_states.values()
        )

    _state = "State.{}".format(id)
    if _state in all_states:
        return render_template(
            '9-states.html',
            state="State: {}".format(all_states[_state].name),
            items=all_states[_state])

    return render_template('9-states.html', items=None)


@app.teardown_appcontext
def teardown_db(exception):
    '''remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
