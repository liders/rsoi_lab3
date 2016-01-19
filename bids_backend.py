import flask
import flask_sqlalchemy
import flask_restless

from config import config

app = flask.Flask(__name__)
app.config['DEBUG'] = config['debug']


app.config['SQLALCHEMY_DATABASE_URI'] = config['bids']['db_uri']
db = flask_sqlalchemy.SQLAlchemy(app)

class Bid(db.Model):
    __tablename__ = 'bid'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    #number_tickets = db.Column(db.Integer, nullable=False)
    #opened_at = db.Column(db.DateTime, nullable=False)
    items = db.relationship('BidItem', cascade='all, delete-orphan')

class BidItem(db.Model):
    __tablename__ = 'bid_item'

    id = db.Column(db.Integer, primary_key=True)
    bid_id = db.Column(db.Integer, db.ForeignKey('bid.id'), nullable=False)
    event_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

db.create_all()


restman = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
restman.create_api(Bid,
    collection_name='bids',
    methods=[
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE'
    ],
)


if __name__ == '__main__':
    app.run(port=config['bids']['port'])

