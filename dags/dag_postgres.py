from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
import requests
from sql_statements import sql_dict

hook = PostgresHook(postgres_conn_id='postgres_my')


def convert_data_non_usd():
    with hook.get_conn() as con:
        cur = con.cursor()
        cur.execute(sql_dict['select_byn'])
        desc = cur.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in cur.fetchall()]
        convert(data)


def convert(data):
    for i in data:
        amount = i.get('price')
        api = 'https://v6.exchangerate-api.com/v6/7dbce18c99cd7ea949727872/pair/BYN/USD/'
        url = api + str(amount)
        responce = requests.get(url)
        c = responce.json()
        i['price'] = c['conversion_result']
        i['currency'] = 'usd'
        val = tuple(i.values())
        write_to_db(val)


def write_to_db(val):
    with hook.get_conn() as con:
        cur = con.cursor()
        cur.execute(sql_dict['insert_converted'], (val))


with DAG(
        dag_id='dag_postgres_v1',
        # default_args=default_args,
        description='my postgres',
        start_date=datetime(2022, 9, 12),
        catchup=False,
        schedule_interval='@daily',
        tags=['dag_postgres_v1']
) as dag:
    task1 = PostgresOperator(
        task_id='Copy_el_BYN', postgres_conn_id='postgres_my', autocommit=False,
        sql=sql_dict['copy_el_usd'])

    task2 = PythonOperator(task_id='convert_data_add_db',
                           python_callable=convert_data_non_usd)

    task1 >> task2
