from ..models.products_models import Product
from flask import request

class ProductController:
    @classmethod
    def get_product_id(self, product_id):
        product=Product.get_product_id(product_id)
        if product is not None:
            data={
                'product_id':product.product_id,
                'product_name':product.product_name,
                'brand':{
                    'brand_id':product.brand_id,
                    'brand_name':product.brand_name
                },
                'category':{
                    'category_id':product.category_id,
                    'category_name':product.category_name
                },
                'model_year':product.model_year,
                'list_price':product.list_price
            }
            return data, 200
        else:
            return({'error': 'No se encontro producto con el id solicitado'}, 404)

    @classmethod
    def get_product(self):
        brand_id=request.args.get('brand_id','')
        category_id=request.args.get('category_id','')
        product=Product.get_product(brand_id, category_id)
        data={
            'products': product,
            'total': len(product)
            }
        return data, 200

    @classmethod
    def create_product(self):
        product=Product(
            product_name=request.form.get('product_name',''),
            brand_id=request.form.get('brand_id',''),
            category_id=request.form.get('category_id',''),
            model_year=request.form.get('model_year',''),
            list_price=request.form.get('list_price','')
        )
        message=Product.create_product(product)
        if message is not None:
            return {'message': message}, 201
        else:
            return {'error':'Complete todos los datos'},400

    @classmethod
    def update_product(self, product_id):
        product=Product(
            product_name=request.form.get('product_name',''),
            brand_id=request.form.get('brand_id',''),
            category_id=request.form.get('category_id',''),
            model_year=request.form.get('model_year',''),
            list_price=request.form.get('list_price','')
        )
        message=Product.update_product(product_id, product)
        if message is not None:
            return {'message': message}, 200
        else:
            return {'error':'No se encontro producto con el id solicitado'},404

    @classmethod
    def delete_product(self, product_id):
        message=Product.delete_product(product_id)
        if message is not None:
            return {}, 204
        else:
            return {'error':'El producto con id solicitado no existe'}, 404