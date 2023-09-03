from flask import Blueprint
from ..controllers.product_controller import ProductController

product_bp = Blueprint('product_bp', __name__)

product_bp.route('/products/<int:product_id>',  methods=['GET'])(ProductController.get_product_id)
product_bp.route('/products',  methods=['GET'])(ProductController.get_product)
product_bp.route('/products',  methods=['POST'])(ProductController.create_product)
product_bp.route('/products/<int:product_id>',  methods=['PUT'])(ProductController.update_product)
product_bp.route('/products/<int:product_id>',  methods=['DELETE'])(ProductController.delete_product)