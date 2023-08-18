import pandas as pd




# Your transformation logic for data set 1
def calculate_total_sales(data):
    data = pd.read_csv(data)
    product_sales = data.groupby('product')['sales'].sum().reset_index()
    return product_sales

sales_data = 'sales_data.csv'
result = calculate_total_sales(sales_data)
print(result)
