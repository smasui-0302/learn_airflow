from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

with DAG(
    dag_id='run_sample_script',
    default_args=default_args,
    description='Pythonスクリプトをbash上で実行するDAG',
    schedule_interval=None,
    catchup=False,
    params={
        'date':'2024-12-31',
        'print_flg': True
    }
) as dag:
    
    task1 = BashOperator(
        task_id='run_sample_script',
        bash_command='echo "$(python /opt/airflow/plugins/sample_script.py --date {{ params.date }})"',
        do_xcom_push=True,
    )

    task2 = BashOperator(
        task_id='print_date',
        bash_command='''{% if params.print_flg %}
                            echo "Date: {{ params.date }}, Result: {{ task_instance.xcom_pull(task_ids="run_sample_script") }}"
                        {% else %}
                            echo "Skip printing"
                        {% endif %}''',
    )

    task1 >> task2