# Прочие документы
* Источник данных изменен на https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset?resource=download&select=cardio_train.csv

* Развертывание экземпляра PostgreSQL в Docker-контейнере и
  минимальная конфигурация, включающая создание базы данных (БД)

```shell
docker run --name test_db -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=test_db -d postgres:11-alpine
```

* Создание учетной записи с надлежащими правами доступа,

1. Вариант [подключиться к бд из контейнера ручками]
    * docker exec -it [id container] bash
    * psql --username=postgres --dbname=postgres
    * \l
    * CREATE USER write_user WITH PASSWORD 'pass' VALID UNTIL '2025-12-31';
    * CREATE ROLE read_user WITH LOGIN PASSWORD 'pass' VALID UNTIL '2025-12-31'; //только для чтения
    * \du
    * \connect example
    * Select * From example;

2. Вариант [docker-compose c инит файлом] не реализован.
    * Пользователей создаем в init.sql

* настройку сетевого доступа для обращения к БД при помощи современных UI-
  инструментов (например, DBeaver или аналогичных сред)
- Скачал DBeaver и через него подключился к БД.  **Выполнено ?** 

 
 