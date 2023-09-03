from flask import Blueprint
from .. controllers.customer_controller import CustomerController

customer_bp = Blueprint('customer_bp', __name__)

customer_bp.route('/customers/<int:customer_id>',  methods=['GET'])(CustomerController.get_customer_id)
customer_bp.route('/customers',  methods=['GET'])(CustomerController.get_customer)
customer_bp.route('/customers',  methods=['POST'])(CustomerController.create_customer)
customer_bp.route('/customers/<int:customer_id>',  methods=['PUT'])(CustomerController.update_customer)
customer_bp.route('/customers/<int:customer_id>',  methods=['DELETE'])(CustomerController.delete_customer)