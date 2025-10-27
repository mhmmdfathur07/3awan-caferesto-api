from models.menu_model import Menu
from config.database import get_db
from flask import jsonify, request
from sqlalchemy.orm import Session

# GET semua menu
def get_all_menus():
    db: Session = next(get_db())
    menus = db.query(Menu).all()
    result = [
        {
            "id": m.id,
            "name": m.name,
            "price": m.price,
            "category": m.category,
            "image_url": m.image_url,
        }
        for m in menus
    ]
    return jsonify(result)

# POST tambah menu
def create_menu():
    db: Session = next(get_db())
    data = request.get_json()
    new_menu = Menu(
        name=data["name"],
        price=data["price"],
        category=data.get("category"),
        image_url=data.get("image_url"),
    )
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return jsonify({"message": "Menu created", "id": new_menu.id}), 201

# GET detail menu
def get_menu_by_id(id):
    db: Session = next(get_db())
    menu = db.query(Menu).filter(Menu.id == id).first()
    if not menu:
        return jsonify({"error": "Menu not found"}), 404
    return jsonify({
        "id": menu.id,
        "name": menu.name,
        "price": menu.price,
        "category": menu.category,
        "image_url": menu.image_url,
    })

# PUT update menu
def update_menu(id):
    db: Session = next(get_db())
    menu = db.query(Menu).filter(Menu.id == id).first()
    if not menu:
        return jsonify({"error": "Menu not found"}), 404

    data = request.get_json()
    menu.name = data.get("name", menu.name)
    menu.price = data.get("price", menu.price)
    menu.category = data.get("category", menu.category)
    menu.image_url = data.get("image_url", menu.image_url)
    db.commit()
    return jsonify({"message": "Menu updated"})

# DELETE hapus menu
def delete_menu(id):
    db: Session = next(get_db())
    menu = db.query(Menu).filter(Menu.id == id).first()
    if not menu:
        return jsonify({"error": "Menu not found"}), 404
    db.delete(menu)
    db.commit()
    return jsonify({"message": "Menu deleted"})
