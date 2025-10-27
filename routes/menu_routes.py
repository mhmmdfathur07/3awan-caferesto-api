from flask import Blueprint
from controllers.menu_controller import (
    get_all_menus,
    create_menu,
    get_menu_by_id,
    update_menu,
    delete_menu,
)

menu_bp = Blueprint("menu_bp", __name__)

menu_bp.route("/", methods=["GET"])(get_all_menus)
menu_bp.route("/", methods=["POST"])(create_menu)
menu_bp.route("/<int:id>", methods=["GET"])(get_menu_by_id)
menu_bp.route("/<int:id>", methods=["PUT"])(update_menu)
menu_bp.route("/<int:id>", methods=["DELETE"])(delete_menu)
