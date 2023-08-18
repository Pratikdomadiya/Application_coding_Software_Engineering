# data_transformation/calculate_customer_revenue_trans.py

# Your transformation logic for data set 2
import pandas as pd
def calculate_customer_revenue(customers_file, orders_file):
    customers = pd.read_csv(customers_file)
    orders = pd.read_csv(orders_file)

    merged_data = pd.merge(customers, orders, on='customer_id')
    merged_data['revenue'] = merged_data['quantity'] * merged_data['unit_price']

    customer_revenue = merged_data.groupby('customer_id')['revenue'].sum().reset_index()
    return customer_revenue

customers_data = 'customers.csv'
orders_data = 'orders.csv'
result = calculate_customer_revenue(customers_data, orders_data)
print(result)

