import pandas as pd
import pyarrow.parquet as pq
from abc import ABC, abstractmethod

# Step 1: Define an interface (or base class)
class DataReader(ABC):
    @abstractmethod
    def read_data(self, file_path):
        pass

# Step 2: Create concrete product classes
class ExcelDataReader(DataReader):
    def read_data(self, file_path):
        return pd.read_excel(file_path)

class CSVDataReader(DataReader):
    def read_data(self, file_path):
        return pd.read_csv(file_path)

class ParquetDataReader(DataReader):
    def read_data(self, file_path):
        table = pq.read_table(file_path)
        return table.to_pandas()

# Step 3: Create a factory class
class DataReaderFactory:
    @staticmethod
    def create_data_reader(file_format):
        if file_format == "excel":
            return ExcelDataReader()
        elif file_format == "csv":
            return CSVDataReader()
        elif file_format == "parquet":
            return ParquetDataReader()
        else:
            raise ValueError("Invalid file format")

# Step 4: Instantiate objects using the factory
factory = DataReaderFactory()

# Read data from Excel
excel_reader = factory.create_data_reader("excel")
excel_data = excel_reader.read_data("data.xlsx")
print("Excel Data:")
print(excel_data)

# Read data from CSV
csv_reader = factory.create_data_reader("csv")
csv_data = csv_reader.read_data("data.csv")
print("\nCSV Data:")
print(csv_data)

# Read data from Parquet
parquet_reader = factory.create_data_reader("parquet")
parquet_data = parquet_reader.read_data("data.parquet")
print("\nParquet Data:")
print(parquet_data)
