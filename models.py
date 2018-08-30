from app import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Interger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    name = db.Column(db.String(40))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

