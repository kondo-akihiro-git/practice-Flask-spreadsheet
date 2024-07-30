from app import db

class Spreadsheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    data = db.Column(db.Text)

    def __repr__(self):
        return f'<Spreadsheet {self.name}>'
