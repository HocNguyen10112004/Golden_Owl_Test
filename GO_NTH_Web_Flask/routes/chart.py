from flask import Blueprint, render_template
import matplotlib.pyplot as plt
import io
import base64
from models import DiemThi

chart_bp = Blueprint("chart", __name__)

@chart_bp.route("/chart")
def chart():
    subjects = ["toan", "ngu_van", "ngoai_ngu", "vat_li", "hoa_hoc", "sinh_hoc", "lich_su", "dia_li", "gdcd"]
    categories = [">=8", "6-8", "4-6", "<4"]
    data = {category: [] for category in categories}

    for subject in subjects:
        data[">=8"].append(DiemThi.query.filter(getattr(DiemThi, subject) >= 8).count())
        data["6-8"].append(DiemThi.query.filter((getattr(DiemThi, subject) >= 6) & (getattr(DiemThi, subject) < 8)).count())
        data["4-6"].append(DiemThi.query.filter((getattr(DiemThi, subject) >= 4) & (getattr(DiemThi, subject) < 6)).count())
        data["<4"].append(DiemThi.query.filter(getattr(DiemThi, subject) < 4).count())

    plt.figure(figsize=(10, 5))
    for category, values in data.items():
        plt.plot(subjects, values, label=category)

    plt.xlabel("Môn học")
    plt.ylabel("Số lượng học sinh")
    plt.title("Thống kê số lượng học sinh theo mức điểm")
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template("chart.html", plot_url=plot_url)
