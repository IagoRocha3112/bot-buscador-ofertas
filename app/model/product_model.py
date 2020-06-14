import sqlite3

class ProductModel():

    def __init__(self):
        # Open connection database
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        # Properties
        self.table = "products"
        
        self.name: str = ""
        self.description: str = ""
        self.price: float = 0.00
        self.site: str = ""


    def read(self):
        self.cursor.execute("""
        SELECT * FROM {0};
        """.format(self.table))

        for row in self.cursor.fetchall():
            print(row)

    def create(self):
        try:
            query = '''
            INSERT INTO products (name, description, price, site)
            VALUES ('{0}', '{1}', {2}, '{3}')
            '''.format(self.name, self.description, self.price, self.site)
            print(query)
            self.cursor.execute(query)
            # Recording in database
            self.connection.commit()
            return True
        except Exception as error:
            print(error)
            return False
       
if __name__ == "__main__":
    model = ProductModel()

    model.name = 'Iago'
    model.description = 'Iago Rocha'
    model.price = 123.45
    model.site = 'https://github.com/IagoRocha3112/'

    model.read()