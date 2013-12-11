from app import db


class Item(db.Model):

    __tablename__ = "items"

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    posted_date = db.Column(db.Date, nullable=False)
    select_field = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    post_body = db.Column(db.String, nullable=False)
