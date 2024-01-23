from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator

'''
Estos parámetros ofrecen una manera de establecer comportamientos predeterminados para tu DAG (Grafo Acíclico Dirigido), 
y pueden ser anulados al definir tareas individuales dentro del DAG.
'''
default_args = {
    'owner': 'leonel',
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1   
}

#defino funciones

def get_data():
    import requests
    res=requests.get('https://randomuser.me/api/')#direccion de la api 
    res=res.json()
    res=res['results'][0]
    return res
    
def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium'] 
    return data  


#Esta función está diseñada para recuperar y dar formato a datos,
# y luego enviarlos a un tema Kafka llamado 'users_created' utilizando el KafkaProducer.

def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging
    res = get_data()
    res = format_data(res)
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time=time.time()
    while True:
        if time.time() > curr_time + 60:
            break
        try:
            res= get_data()
            res=format_data(res)
            producer.send('users_created',json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error ocurred: {e}')
            continue
    



#Creamos el dag que nos sirve de punto de entrada

with DAG('user_automation',
         default_args=default_args,
         schedule='@daily',
         catchup=False)as dag:
    # usamos  el operador de python para ejecutar las funciones
    streaming_task=PythonOperator(
        task_id='stream_data_from_api',
        python_callable= stream_data
    )
    



