from datetime import timedelta

config = {
    'debug': True,

    'website': {
        'port': 5050,
        'session_expires_after': timedelta(weeks=2),
    },       

    'sessions': {
        'port': 5051,
        'db_uri': 'sqlite:///:memory:',
    },       
    'users': {
        'port': 5052,
        'db_uri': 'sqlite:///db/users',
    },       
    'events': {
        'port': 5053,
        'db_uri': 'sqlite:///db/events',
    },       
    'bids': {
        'port': 5054,
        'db_uri': 'sqlite:///db/bids',
    },       
}
