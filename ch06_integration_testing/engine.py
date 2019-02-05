from sqlite3 import connect
from os.path import exists

class Phonebook():
    def __init__(self):
        #initializes path to db
        self.db_path = 'C:/Users/crypteye/Desktop/Phonebook_webapp/Phonebook_webapp/static/db/Phonebook.db'


    def check_db(self):
        #checks if database exist. if it does it creates a new Phonebook class attribute 'db_exist' which is set to True
        if exists(self.db_path):
            return True
        #and False if not
        else:
            return False


    def connect_db(self):
        try:
            if self.check_db():
                self.connection = connect(self.db_path)
                self.cursor = self.connection.cursor()
            else:
                print('Database Does Not Exist.... :-(')
                return None
        except:
            print("Confused ......")



    def query_db(self,query, params=None):
        try:
            self.connect_db()
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.results = self.cursor.fetchall()
            self.connection.close()
        except Exception as e:
            print(e)

    def get_categories(self):
        try:
            query = "SELECT business_category FROM business;"
            self.query_db(query)
            return self.results
        except Exception as e:
            print(e)

    def get_cities(self):
        try:
            query = "SELECT address_line_2 FROM business;"
            self.query_db(query)
            return self.results
        except Exception as e:
            print(e)

    def get_all_businesses(self):
        try:
            query = "SELECT * FROM business;"
            self.query_db(query)
            return self.results
        except Exception as e:
            print('oops: something went wrong')
            print(e)


    def get_all_people(self):
        try:
            query = "SELECT * FROM people;"
            self.query_db(query)
            return self.results
        except Exception as e:
            print(e)

    def find_business(self,biz_name=None, category=None, location=None):
        ##my very lazy but efficient all purpose 'find-business' function

        if biz_name and category and location:
            try:
                query = "SELECT * FROM business where UPPER(business_name) LIKE UPPER('%%%s%%') AND UPPER(business_category) LIKE UPPER('%%%s%%') AND UPPER(address_line_2) LIKE UPPER('%%%s%%')" % (biz_name,category,location)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif biz_name and category:
            try:
                query = "SELECT * FROM business where UPPER(business_name) LIKE UPPER('%%%s%%') AND UPPER(business_category) LIKE UPPER('%%%s%%')" % (biz_name,category)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif biz_name and location:
            try:
                query = "SELECT * FROM business where UPPER(business_name) LIKE UPPER('%%%s%%') AND UPPER(address_line_2) LIKE UPPER('%%%s%%')" % (biz_name,location)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif category and location:
            try:
                query = "SELECT * FROM business where UPPER(business_category) LIKE UPPER('%%%s%%') AND UPPER(address_line_2) LIKE UPPER('%%%s%%')" % (category,location)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif biz_name:
            try:
                query = "SELECT * FROM business where UPPER(business_name) LIKE UPPER('%%%s%%')" % (biz_name)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif category:
            try:
                query = "SELECT * FROM business where UPPER(business_category) LIKE UPPER('%%%s%%')" % (category)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)

        elif location:
            try:
                query = "SELECT * FROM business where UPPER(address_line_2) LIKE UPPER('%%%s%%')" % (location)
                self.query_db(query)
                return self.results
            except Exception as e:
                print(e)
        else:
            self.results = [('Nothing Found')]
            return self.results
