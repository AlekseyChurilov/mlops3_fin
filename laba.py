from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
from datetime import datetime, timedelta

args = {
    'owner': 'alex',
    'start_date':datetime(2018, 11, 1),
    'provide_context':True
}

with DAG('tsch', description='pffffff', schedule_interval='*/1 * * * *',  catchup=False, defa>
    t1 = BashOperator(
        task_id='task_1',
        bash_command='python3 /home/data1/lab1/data_creation.py',
        dag=dag)

    t2 = BashOperator(
        task_id='task_2',
        bash_command='python3 /home/data1/lab1/data_preprocessing.py',
        dag=dag)

    t3 = BashOperator(
        task_id='task_3',
        bash_command='python3 /home/data1/lab1/model_preparation.py',
        dag=dag)

    t4 = BashOperator(
        task_id='task_4',
        bash_command='python3 /home/data1/lab1/model_testing.py',
        dag=dag)

t1 >> t2 >> t3 >> t4
