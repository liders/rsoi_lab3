import flask
import flask_sqlalchemy
import flask_restless

from config import config

app = flask.Flask(__name__)
app.config['DEBUG'] = config['debug']


app.config['SQLALCHEMY_DATABASE_URI'] = config['events']['db_uri']
db = flask_sqlalchemy.SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False, unique=True)
    date = db.Column(db.Unicode, nullable=False)
    description = db.Column(db.Unicode, nullable=True, default=None)
    organizer = db.Column(db.Unicode, nullable=True, default=None)

db.create_all()


restman = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
restman.create_api(Event,
    collection_name='events',
    methods=[
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE'
    ],
)


if __name__ == '__main__':
    app.run(port=config['events']['port'])

