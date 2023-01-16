from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow import DAG
from datetime import datetime
import os




with DAG(dag_id="example_spark_job",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
    spark_task = SparkKubernetesOperator(
        task_id = "example_spark_job",
        application_file = "./application.yaml",
        namespace = "compute-plane"
    )