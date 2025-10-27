from flask import jsonify, request
from config.database import get_db
from models.menu_model import Menu
from sqlalchemy.orm import Session

# GET semua menu
def get_all_menus():
    db: Session = next(get_db())
    data = db.query(Menu).all()
    return jsonify([
        {
            "id": m.id,
            "name": m.name,
            "price": m.price,
            "category": m.category,
            "image_url": m.image_url
        }
        for m in data
    ])

# GET menu berdasarkan ID
def get_menu_by_id(id):
    db: Session = next(get_db())
    m = db.query(Menu).filter(Menu.id == id).first()
    if not m:
        return jsonify({"message": "Menu not found"}), 404
    return jsonify({
        "id": m.id,
        "name": m.name,
        "price": m.price,
        "category": m.category,
        "image_url": m.image_url
    })

# POST tambah menu baru
def add_menu():
    db: Session = next(get_db())
    body = request.json

    new_menu = Menu(
        name=body.get("name"),
        price=body.get("price"),
        category=body.get("category"),
        image_url=body.get("image_url")
    )
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)

    return jsonify({
        "message": "Menu berhasil ditambahkan",
        "id": new_menu.id
    })

# PUT update menu
def update_menu(id):
    db: Session = next(get_db())
    body = request.json
    m = db.query(Menu).filter(Menu.id == id).first()
    if not m:
        return jsonify({"message": "Menu not found"}), 404

    m.name = body.get("name", m.name)
    m.price = body.get("price", m.price)
    m.category = body.get("category", m.category)
    m.image_url = body.get("image_url", m.image_url)

    db.commit()
    db.refresh(m)

    return jsonify({"message": "Menu berhasil diupdate"})

# DELETE menu
def delete_menu(id):
    db: Session = next(get_db())
    m = db.query(Menu).filter(Menu.id == id).first()
    if not m:
        return jsonify({"message": "Menu not found"}), 404

    db.delete(m)
    db.commit()
    return jsonify({"message": "Menu berhasil dihapus"})
