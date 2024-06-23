from flask import Flask, send_from_directory
from blog.routes import blog_blueprint
from blog.models import db
from config import Config
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(blog_blueprint)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
