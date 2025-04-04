from app import db
from datetime import date


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    reg_code = db.Column(db.String(7), nullable=False, unique=True)
    established_date = db.Column(db.Date, nullable=False)
    capital = db.Column(db.Integer, nullable=False)

    shareholders = db.relationship('Shareholder', backref='company', lazy=True)

    def __repr__(self):
        return f"<Company {self.name} (Reg.kood: {self.reg_code})>"


class Shareholder(db.Model):
    __tablename__ = 'shareholder'

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

    shareholder_type = db.Column(db.String(10), nullable=False)

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    personal_code = db.Column(db.String(20))

    legal_name = db.Column(db.String(100))
    legal_reg_code = db.Column(db.String(20))

    share_amount = db.Column(db.Integer, nullable=False)
    founder = db.Column(db.Boolean, default=False)

    def __repr__(self):
        if self.shareholder_type == 'physical':
            return f"<Shareholder {self.first_name} {self.last_name} (Osakaal: {self.share_amount}€)>"
        else:
            return f"<Shareholder {self.legal_name} (Reg.kood: {self.legal_reg_code}, Osakaal: {self.share_amount}€)>"
