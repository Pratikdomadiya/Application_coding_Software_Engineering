# dags/dag1.py
"""
Remember to replace placeholders with actual values in the code samples. This structure allows you to
manage your code more effectively, improve reusability, and enhance maintainability.
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from etl_processing.etl import perform_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('data_migration_dag1', default_args=default_args, schedule_interval=timedelta(days=1))

def run_etl_task():
    perform_etl("input_file.csv", "your-s3-bucket", "your-access-key", "your-secret-key")

etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=run_etl_task,
    dag=dag,
)
