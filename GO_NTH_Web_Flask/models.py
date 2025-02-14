from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DiemThi(db.Model):
    __tablename__ = "diem_thi"

    sbd = db.Column(db.BigInteger, primary_key=True)
    toan = db.Column(db.Float)
    ngu_van = db.Column(db.Float)
    ngoai_ngu = db.Column(db.Float)
    vat_li = db.Column(db.Float)
    hoa_hoc = db.Column(db.Float)
    sinh_hoc = db.Column(db.Float)
    lich_su = db.Column(db.Float)
    dia_li = db.Column(db.Float)
    gdcd = db.Column(db.Float)
    ma_ngoai_ngu = db.Column(db.String(2))
