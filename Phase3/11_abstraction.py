from abc import ABC, abstractmethod

# 1. THE ABSTRACT BASE CLASS
# It must inherit from 'ABC' to make it an abstract class
class Database(ABC):

    def __init__(self, connection_string):
        self.connection_string = connection_string

    # An abstract method has no implementation here.
    # It forces child classes to write their own version.
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

# 2. THE CONCRETE CHILD CLASS 1
class MySQLDatabase(Database):
    # if we don't implement connect() and execute_query() python will throw an error
    def connect(self):
        print(f"Connecting securely to MySQL instance at: {self.connection_string}")

    def execute_query(self, query):
        print(f"Running MySQL engine to excute: '{query}'")

# 3. THE CONCRETE CHILD CLASS 2
class PostgreSQLDatabase(Database):
    def connect(self):
        print(f"Opening Postgres connection pool at: {self.connection_string}")

    def execute_query(self, query):
        print(f"Optimizing Postgres planner for query: '{query}'")

# ---- Execute -----
print("---- 1. Trying to instantiate the Abstract Class ----")
try:
    # This will crash because you cannot build a generic database object!
    db = Database("localhost: 5432")
except TypeError as e:
    print(f"Blocked! Error: {e}")

print("\n---2. Working with Concrete Subclasses ----")
# Using the classes that properly fulfilled the abstract contract
my_sql = MySQLDatabase("mysql://roor@127.0.0.1/db")
Postgres = PostgreSQLDatabase("postgresql://postgres@localhost:5432/prod")

my_sql.connect()
my_sql.execute_query("SELECT * FROM users;")
      
print()

Postgres.connect()
Postgres.execute_query("SELCT * FROM logs;")