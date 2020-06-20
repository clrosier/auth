from .. import db, flask_bcrypt

class Blog(db.Model):
    """ Blog model """
    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    is_private = db.Column(db.Boolean, default=False)
    creation_date = db.Column(db.DateTime, index=True, nullable=False)
    created_by = db.Column(db.String(50), db.ForeignKey('bloggers.id'))

    def __repr__(self):
        return "<Blog '{}'>".format(self.title)

