from engine import *



class TestEngine():
    def __init__(self):
        self.pb = Phonebook()

    def test_check_db(self):
        self.checked = self.pb.check_db()
        return self.checked

    def test_connect_db(self):
        self.test_check_db()

        if self.checked:
            connected = self.pb.connect_db()
            if connected:
                self.connected = True
                return self.connected
            else:
                self.connected = False
                return self.connected
        else:
            print("Database Does not Exist: Connection Test Failed :-(")

    def test_query_db(self):
        query ="SELECT * FROM business;"
        results = self.pb.query_db(query)
        if results:
            self.queried = True
        else:
            self.query = False

    def run_tests(self):
        print(self.test_check_db())
        print(self.test_connect_db())
        print(self.test_query_db())


if __name__ == "__main__":
    newTest = TestEngine()
    newTest.run_tests()