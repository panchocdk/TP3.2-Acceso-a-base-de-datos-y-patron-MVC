from ..database import DatabaseConnection

class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, phone=None, email=None, street=None, city=None, state=None, zip_code=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    @classmethod
    def get_customer_id(self, cust_id):
        query="SELECT first_name, last_name, phone, email, street, city, state, zip_code FROM sales.customers WHERE customer_id = %s;"
        params=(cust_id,)
        result=DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Customer(
                customer_id=cust_id,
                first_name=result[0],
                last_name=result[1],
                phone=result[2],
                email=result[3],
                street=result[4],
                city=result[5],
                state=result[6],
                zip_code=result[7]
            )
        else:
            return None
        
    @classmethod
    def get_customer(self, state):
        if state!='':
            query="SELECT * FROM sales.customers WHERE state=%s;"
            params=(state,)
            results=DatabaseConnection.fetch_all(query, params)
        else:
            query="SELECT * FROM sales.customers;"
            results=DatabaseConnection.fetch_all(query)
        if results is not None:
            customers=[]
            for result in results:
                customers.append({
                    'customer_id':result[0],
                    'first_name':result[1],
                    'last_name':result[2],
                    'phone':result[3],
                    'email':result[4],
                    'street':result[5],
                    'city':result[6],
                    'state':result[7],
                    'zip_code':result[8]
                })
            return customers
        else:
            return None

    @classmethod
    def create_customer(self,customer):
        query="INSERT INTO sales.customers (first_name, last_name, phone, email, street, city, state, zip_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        if customer.first_name!='' and customer.last_name!='' and customer.email!='':
            params=(customer.first_name, customer.last_name, customer.phone, customer.email, customer.street, customer.city,customer.state,customer.zip_code)
            DatabaseConnection.execute_query(query, params)
            message='Cliente creado con exito'
        else:
            message=None
        return message

    @classmethod
    def update_customer(self, cust_id, customer):
        if self.check_customer(cust_id):
            query="UPDATE sales.customers SET"
            params=[]
            if customer.first_name:
                query += ' first_name=%s,'
                params.append(customer.first_name)
            if customer.last_name:
                query += ' last_name=%s,'
                params.append(customer.last_name)
            if customer.phone:
                query += ' phone=%s,'
                params.append(customer.phone)
            if customer.email:
                query += ' email=%s,'
                params.append(customer.email)
            if customer.street:
                query += ' street=%s,'
                params.append(customer.street)
            if customer.city:
                query += ' city=%s,'
                params.append(customer.city)
            if customer.state:
                query += ' state=%s,'
                params.append(customer.state)
            if customer.zip_code:
                query += ' zip_code=%s,'
                params.append(customer.zip_code)
            query=query.rstrip(',')
            query += ' WHERE customer_id = %s'
            params.append(cust_id)
            DatabaseConnection.execute_query(query, params)
            message='Cliente actualizado con exito'
        else:
            message=None
        return message

        
    def check_customer(c_id):
        query="SELECT COUNT(*) FROM sales.customers WHERE customer_id = %s"
        params=(c_id,)
        result=DatabaseConnection.fetch_one(query, params)[0]
        if result>0:
            return True
        else:
            return False
        
    @classmethod
    def delete_customer(self, cust_id):
        if self.check_customer(cust_id):
            query="DELETE FROM sales.customers WHERE customer_id = %s"
            params=(cust_id,)
            DatabaseConnection.execute_query(query, params)
            message='Cliente eliminado con exito'
        else:
            message=None
        return message