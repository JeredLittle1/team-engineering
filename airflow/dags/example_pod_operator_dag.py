from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow import DAG
from datetime import datetime
import os


with DAG(dag_id="test_kubernetes_pod_operator",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
    k = KubernetesPodOperator(
        name="hello-world",
        image="debian", # Replace with any image!
        cmds=["bash", "-cx"],
        arguments=["echo", "Hello World!"],
        labels={"foo": "bar"},
        task_id="test",
        in_cluster=True,
        get_logs=True,
    )