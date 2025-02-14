from flask import Blueprint, render_template, request, flash
from models import DiemThi

search_bp = Blueprint("search", __name__)

@search_bp.route("/search", methods=["GET", "POST"])
def search():
    student = None
    error_message = None

    if request.method == "POST":
        sbd = request.form.get("sbd")
        if not sbd:
            error_message = "Vui lòng nhập số báo danh." 
        elif not sbd.isdigit():
            error_message = "Số báo danh phải là số nguyên hợp lệ."
        else:
            student = DiemThi.query.filter_by(sbd=int(sbd)).first()
            if not student:
                error_message = f"Không tìm thấy kết quả cho SBD {sbd}."

    return render_template("search.html", student=student, error_message=error_message)
