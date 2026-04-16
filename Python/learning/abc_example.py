from abc import ABC, abstractmethod

class IDataSource(ABC):
    @abstractmethod
    def get_data(self, query):
        pass

    @abstractmethod
    def save_data(self, data):
        pass

class DatabaseSource(IDataSource):
    def get_data(self, query):
        # Implementation to retrieve data from a database
        print(f"Retrieving data from database with query: {query}")
        return {"result": "database data"}

    def save_data(self, data):
        # Implementation to save data to a database
        print(f"Saving data to database: {data}")

# Example usage
db_source = DatabaseSource()
db_source.get_data("SELECT * FROM users")
db_source.save_data({"name": "Alice"})