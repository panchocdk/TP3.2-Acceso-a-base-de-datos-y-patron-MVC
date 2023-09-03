from ..database import DatabaseConnection

class Product:
    def __init__(self, product_id=None, product_name=None, brand_id=None, brand_name=None, category_id=None, category_name=None, model_year=None, list_price=None):
        self.product_id=product_id
        self.product_name=product_name
        self.brand_id=brand_id
        self.brand_name=brand_name
        self.category_id=category_id
        self.category_name=category_name
        self.model_year=model_year
        self.list_price=list_price

    @classmethod
    def get_product_id(self, prod_id):
        query="SELECT p.product_name, b.brand_id, b.brand_name, c.category_id, c.category_name, p.model_year, p.list_price\
                FROM  production.products p\
                INNER JOIN production.brands b on p.brand_id = b.brand_id\
                INNER JOIN production.categories c on p.category_id = c.category_id\
                WHERE product_id = %s"
        params=(prod_id,)
        result=DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Product(
                product_id=prod_id,
                product_name=result[0],
                brand_id=result[1],
                brand_name=result[2],
                category_id=result[3],
                category_name=result[4],
                model_year=result[5],
                list_price=result[6]
            )
        else:
            return None

    @classmethod
    def get_product(self, b_id, c_id):
        if b_id!='' or c_id!='':
            query="SELECT p.product_id, p.product_name, b.brand_id, b.brand_name, c.category_id, c.category_name, p.model_year, p.list_price\
                    FROM  production.products p\
                    INNER JOIN production.brands b on p.brand_id = b.brand_id\
                    INNER JOIN production.categories c on p.category_id = c.category_id\
                    WHERE b.brand_id = %s OR c.category_id = %s"
            params=(b_id, c_id)
            results=DatabaseConnection.fetch_all(query, params)
        else:
            query="SELECT p.product_id, p.product_name, b.brand_id, b.brand_name, c.category_id, c.category_name, p.model_year, p.list_price\
                    FROM  production.products p\
                    INNER JOIN production.brands b on p.brand_id = b.brand_id\
                    INNER JOIN production.categories c on p.category_id = c.category_id"
            results=DatabaseConnection.fetch_all(query)
        if results is not None:
            products=[]
            for result in results:
                products.append({
                    'product_id':result[0],
                    'product_name':result[1],
                    'brand':{
                        'brand_id':result[2],
                        'brand_name':result[3]
                    },
                    'category':{
                        'category_id':result[4],
                        'category_name':result[5]
                    },
                    'model_year':result[6],
                    'list_price':result[7]
                })
            return products
        else:
            return None

    @classmethod
    def create_product(self,product):
        query="INSERT INTO production.products (product_name, brand_id, category_id, model_year, list_price) VALUES (%s,%s,%s,%s,%s)"
        if product.product_name!='' and product.brand_id!='' and product.category_id!='' and product.model_year!='' and product.list_price!='':
            params=(product.product_name, product.brand_id, product.category_id, product.model_year, product.list_price)
            DatabaseConnection.execute_query(query, params)
            message='Producto creado con exito'
        else:
            message=None
        return message

    @classmethod
    def update_product(self, prod_id, product):
        if self.check_product(prod_id):
            query="UPDATE production.products SET"
            params=[]
            if product.product_name:
                query += ' product_name=%s,'
                params.append(product.product_name)
            if product.brand_id:
                query += ' brand_id=%s,'
                params.append(product.brand_id)
            if product.category_id:
                query += ' category_id=%s,'
                params.append(product.category_id)
            if product.model_year:
                query += ' model_year=%s,'
                params.append(product.model_year)
            if product.list_price:
                query += ' list_price=%s,'
                params.append(product.list_price)
            query=query.rstrip(',')
            query += ' WHERE product_id = %s'
            params.append(prod_id)
            DatabaseConnection.execute_query(query, params)
            message='Producto actualizado con exito'
        else:
            message=None
        return message

    def check_product(p_id):
        query="SELECT COUNT(*) FROM production.products WHERE product_id = %s"
        params=(p_id,)
        result=DatabaseConnection.fetch_one(query, params)[0]
        if result>0:
            return True
        else:
            return False

    @classmethod
    def delete_product(self, prod_id):
        if self.check_product(prod_id):
            query="DELETE FROM production.products WHERE product_id = %s"
            params=(prod_id,)
            DatabaseConnection.execute_query(query, params)
            message='Producto eliminado con exito'
        else:
            message=None
        return message