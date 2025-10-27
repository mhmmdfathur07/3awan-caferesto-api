from flask import Flask
from config.database import engine, Base
from routes.web import web
import models.menu_model  # register model

app = Flask(__name__)

# Buat tabel otomatis (jika belum ada di database)
Base.metadata.create_all(bind=engine)

# Daftarkan route
app.register_blueprint(web)

@app.route("/")
def home():
    return {"message": "3awan Cafe & Resto API is running 🚀"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
