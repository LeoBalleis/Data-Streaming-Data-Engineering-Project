# Transmisión de Datos en Tiempo Real | Proyecto de Ingeniería de Datos

## Introducción 

Este proyecto cubre cada etapa, desde la ingestión de datos hasta el procesamiento y finalmente el almacenamiento. Utilizando un stack tecnológico robusto que incluye Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark y Cassandra. Todo está contenerizado con Docker para facilitar la implementación y escalabilidad.

## Arquitectura del Sistema

![Arquitectura del Sistema](./Data%20engineering%20architecture.png)

El proyecto está diseñado con los siguientes componentes:

- **Fuente de Datos**: Utilizamos la API randomuser.me para generar datos de usuario aleatorios en nuestra pipeline.
- **Apache Airflow**: Responsable de orquestar la pipeline y almacenar los datos recuperados en una base de datos PostgreSQL.
- **Apache Kafka y Zookeeper**: Se utiliza para transmitir datos desde PostgreSQL hacia el motor de procesamiento.
- **Control Center y Schema Registry**: Ayuda en la supervisión y gestión de esquemas de nuestros flujos de Kafka.
- **Apache Spark**: Para el procesamiento de datos con sus nodos maestros y trabajadores.
- **Cassandra**: Donde se almacenarán los datos procesados.

## Objetivos

- Configurar una tubería de datos con Apache Airflow
- Streaming de datos en tiempo real con Apache Kafka
- Sincronización distribuida con Apache Zookeeper
- Técnicas de procesamiento de datos con Apache Spark
- Soluciones de almacenamiento de datos con Cassandra y PostgreSQL
- Contenerizar toda tu configuración de ingeniería de datos con Docker

## Tecnologías

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker
