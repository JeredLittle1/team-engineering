from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.hooks.base import BaseHook  # Deprecated in Airflow 2
import os

def helloWorld():
    # MY_COOL_AIRFLOW_CONNECTION
    print(os.environ)
    connection = BaseHook.get_connection("my_cool_airflow_connection")
    #print(f"{connection.host} {connection.schema}!")

with DAG(dag_id="test_connections",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
    task1 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld)