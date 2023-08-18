import pandas as pd




# Your transformation logic for data set 1
import pandas as pd

def calculate_total_sales(input_file):
    """
    Calculate total sales for each product.

    Args:
        input_file (str): Path to the CSV file containing sales data.

    Returns:
        pandas.DataFrame: DataFrame with product names and their total sales.
    """
    data = pd.read_csv(input_file)
    product_sales = data.groupby('product')['sales'].sum().reset_index()
    return product_sales

sales_data = 'sales_data.csv'
result = calculate_total_sales(sales_data)
print(result)
