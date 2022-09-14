from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from sql_statements import sql_dict


with DAG(
        dag_id='create_db_dag',
        # default_args=default_args,
        description='my postgres',
        start_date=datetime(2022, 9, 12),
        catchup=False,
        schedule_interval='@once',
        tags=['dag_postgres_v1']
) as dag:
    task1 = PostgresOperator(
        task_id='Create_table', postgres_conn_id='postgres_my', autocommit=True,
        sql=sql_dict['create_table'])

    task1
