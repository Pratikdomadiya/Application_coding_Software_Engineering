import sqlite3
import psycopg2
from abc import ABC, abstractmethod

# Step 1: Define an interface (or base class)
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

# Step 2: Create concrete product classes
class SQLiteDatabaseConnection(DatabaseConnection):
    def connect(self, database_name):
        return sqlite3.connect(database_name)

class PostgreSQLDatabaseConnection(DatabaseConnection):
    def connect(self, host, port, database_name, user, password):
        return psycopg2.connect(
            host=host,
            port=port,
            database=database_name,
            user=user,
            password=password
        )

# Step 3: Create a factory class
class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(connection_type, *args, **kwargs):
        if connection_type == "sqlite":
            return SQLiteDatabaseConnection()
        elif connection_type == "postgresql":
            return PostgreSQLDatabaseConnection()
        else:
            raise ValueError("Invalid database connection type")

# Step 4: Instantiate objects using the factory
factory = DatabaseConnectionFactory()

# Create SQLite connection
sqlite_connection = factory.create_connection("sqlite")
sqlite_db = sqlite_connection.connect("my_database.db")
print("SQLite Connection:", sqlite_db)

# Create PostgreSQL connection
pg_connection = factory.create_connection("postgresql")
pg_db = pg_connection.connect(
    host="localhost",
    port=5432,
    database_name="mydb",
    user="myuser",
    password="mypassword"
)
print("PostgreSQL Connection:", pg_db)
