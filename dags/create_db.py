from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator

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
        sql="""
        create table if not exists orders(
        product_name varchar,
        price real,
        currency varchar,
        purchase_date varchar);INSERT INTO orders(product_name,price,currency,purchase_date)
        VALUES ('acer',1540,'byn','02082022'),
        ('toshiba',1890,'byn','28012022'),
        ('hp',540,'usd','21062022'),
        ('apple',1400,'usd','26022022');
        create table if not exists sold(id serial primary key,
        product_name varchar,
        price real,
        currency varchar,
        purchase_date varchar)""")

    task1
