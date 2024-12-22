from flask import Flask
from routes import g_insights
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Register the Blueprint for routes
app.register_blueprint(g_insights, url_prefix='/api')


@app.route('/')
def home():
    return "Todo App is running!"

if __name__ == '__main__':
    app.run(debug=True)
