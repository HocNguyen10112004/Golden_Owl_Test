from flask import Blueprint, render_template
from models import DiemThi
from sqlalchemy.sql import func

top10_bp = Blueprint("top10", __name__)

@top10_bp.route("/top10_khoiA")
def top10_khoiA():
    top_10_students = (
        DiemThi.query.order_by((DiemThi.toan + DiemThi.vat_li + DiemThi.hoa_hoc).desc())
        .limit(10)
        .all()
    )
    if len(top_10_students) == 10:
        min_score = top_10_students[-1].toan + top_10_students[-1].vat_li + top_10_students[-1].hoa_hoc
    else:
        min_score = None  # take all if <10
    if min_score is not None:
        top_students = (
            DiemThi.query.filter((DiemThi.toan + DiemThi.vat_li + DiemThi.hoa_hoc) >= min_score)
            .order_by((DiemThi.toan + DiemThi.vat_li + DiemThi.hoa_hoc).desc())
            .all()
        )
    else:
        top_students = top_10_students  

    return render_template("top10.html", top_students=top_students)
