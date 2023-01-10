FROM apache/airflow:2.5.0-python3.10

USER airflow
COPY ./requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt -c https://raw.githubusercontent.com/apache/airflow/constraints-2-5/constraints-3.10.txt
