from app import db,lm
from flask_login import UserMixin

#ROLE_USER = 0
#ROLE_ADMIN = 1

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), nullable=False, index = True, unique = True)
    email = db.Column(db.String(120), nullable = True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)

#    role = db.Column(db.SmallInteger, default = ROLE_USER)

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
