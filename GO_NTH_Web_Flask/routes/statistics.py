from flask import Blueprint, render_template
from models import DiemThi

statistics_bp = Blueprint("statistics", __name__)

@statistics_bp.route("/statistics")
def statistics():
    subjects = ["toan", "ngu_van", "ngoai_ngu", "vat_li", "hoa_hoc", "sinh_hoc", "lich_su", "dia_li", "gdcd"]
    subject_stats = {}

    for subject in subjects:
        subject_stats[subject] = {
            ">=8": DiemThi.query.filter(getattr(DiemThi, subject) >= 8).count(),
            "6-8": DiemThi.query.filter((getattr(DiemThi, subject) >= 6) & (getattr(DiemThi, subject) < 8)).count(),
            "4-6": DiemThi.query.filter((getattr(DiemThi, subject) >= 4) & (getattr(DiemThi, subject) < 6)).count(),
            "<4": DiemThi.query.filter(getattr(DiemThi, subject) < 4).count(),
        }

    return render_template("statistics.html", subject_stats=subject_stats)
