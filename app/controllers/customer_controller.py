from ..models.customers_models import Customer
from flask import request

class CustomerController:
    @classmethod
    def get_customer_id(self, customer_id):
        customer=Customer.get_customer_id(customer_id)
        if customer is not None:
            data={
                'customer_id':customer.customer_id,
                'first_name':customer.first_name,
                'last_name':customer.last_name,
                'phone':customer.phone,
                'email':customer.email,
                'street':customer.street,
                'city':customer.city,
                'state':customer.state,
                'zip_code':customer.zip_code
            }
            return data, 200
        else:
            return({'error': 'No se encontro cliente con el id solicitado'}, 404)
    
    @classmethod
    def get_customer(self):
        state=request.args.get('state','')
        customer=Customer.get_customer(state)
        data={
            'customers':customer,
            'total': len(customer)
            }
        return data, 200
    
    @classmethod
    def create_customer(self):
        customer=Customer(
            first_name=request.form.get('first_name',''),
            last_name=request.form.get('last_name',''),
            phone=request.form.get('phone'),
            email=request.form.get('email',''),
            street=request.form.get('street'),
            city=request.form.get('city'),
            state=request.form.get('state'),
            zip_code=request.form.get('zip_code')
        )
        message=Customer.create_customer(customer)
        if message is not None:
            return {'message': message}, 201
        else:
            return {'error':'Complete los datos obligatorios: first_name, last_name, email'},400

    @classmethod
    def update_customer(self, customer_id):
        customer=Customer(
            first_name=request.form.get('first_name',''),
            last_name=request.form.get('last_name',''),
            phone=request.form.get('phone',''),
            email=request.form.get('email',''),
            street=request.form.get('street',''),
            city=request.form.get('city',''),
            state=request.form.get('state',''),
            zip_code=request.form.get('zip_code','')
        )
        message=Customer.update_customer(customer_id, customer)
        if message is not None:
            return {'message': message}, 200
        else:
            return {'error':'No se encontro cliente con el id solicitado'},404

    @classmethod
    def delete_customer(self, customer_id):
        message=Customer.delete_customer(customer_id)
        if message is not None:
            return {}, 204
        else:
            return {'error':'El cliente con id solicitado no existe'}, 404