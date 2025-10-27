from flask import Flask
from flask_cors import CORS
from config.database import engine, Base
from routes.menu_routes import menu_bp

app = Flask(__name__)
CORS(app)

# Buat tabel otomatis kalau belum ada
Base.metadata.create_all(bind=engine)

# Register blueprint untuk route menu
app.register_blueprint(menu_bp, url_prefix="/api/menus")

@app.route("/")
def home():
    return {"message": "3awan Cafe & Resto API is running!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
