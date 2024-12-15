from flask import Flask
from config import Config
from models import db, ma
from routes import todo_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

# Register the Blueprint for routes
app.register_blueprint(todo_bp, url_prefix='/api')

# Initialize the database before the app runs
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Todo App is running!"

if __name__ == '__main__':
    app.run(debug=True)
