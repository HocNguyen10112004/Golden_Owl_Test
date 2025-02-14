from flask import Flask
from config import Config
from models import db
from routes.home import home_bp
from routes.search import search_bp
from routes.statistics import statistics_bp
from routes.chart import chart_bp
from routes.top10 import top10_bp  

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(statistics_bp)
app.register_blueprint(chart_bp)
app.register_blueprint(top10_bp)
app.register_blueprint(search_bp)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
