import psycopg2
from Settings import get_config


class DBConnector:  # Класс для подключения к базе данных
    # Параметры подключения к базе данных
    host = get_config()["DB_HOST"]
    port = get_config()["POSTGRES_PORT"]
    database = get_config()["POSTGRES_DB"]
    user = get_config()["POSTGRES_USER"]
    password = get_config()["POSTGRES_PASSWORD"]

    # Создаем соединение
    connection = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
    connection.autocommit = True  # TODO оставил пока так (connection.commit())
    # Получаем курсор для выполнения запросов
    cursor = connection.cursor()

    init_table_query = """
    DROP TABLE IF EXISTS example;
    CREATE TABLE example (active integer, alco integer, ap_hi integer, ap_lo integer, cardio integer, cholesterol integer, gluc integer, height integer, smoke integer, weight float(53), id bigint not null, age integer, gender integer, primary key (id));"""
    cursor.execute(init_table_query)

    init_users_query = """
    SELECT 'CREATE ROLE read_user'
    WHERE NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'read_user');
    ALTER USER read_user WITH PASSWORD 'pass';

    SELECT 'CREATE ROLE write_user'
    WHERE NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'read_user');
    ALTER USER write_user WITH PASSWORD 'pass' VALID UNTIL '2025-12-31';
    """
    cursor.execute(init_users_query)

    init_data_query = (
        "INSERT INTO example (id,age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,cardio)"
        "values (11, 11, 11, 11, 11.0, 11, 11, 11, 11, 11,11, 11, 111111); ")
    cursor.execute(init_data_query)

    def get_all_tables(self):
        # Выполняем запрос
        query = "SELECT * FROM pg_catalog.pg_tables WHERE schemaname='public';"
        cursor = self.connection.cursor()
        cursor.execute(query)
        for el in cursor:
            print(el)
        # Извлекаем результаты запроса
        results = cursor.fetchall()
        return results

    def close(self):
        # Закрываем курсор и соединение
        self.cursor.close()
        self.connection.close()

    def get_table_name(self, table_name):
        cursor = self.connection.cursor()
        query = "SELECT * FROM pg_catalog.pg_tables WHERE schemaname='public' AND tablename='{}';".format(table_name)
        cursor.execute(query)
        for el in cursor:
            print(el)
        results = cursor.fetchall()
        cursor.close()
        self.connection.close()
        return results

    def insert_data(self, row):
        cursor = self.connection.cursor()
        print(row[12])
        query = ("INSERT INTO example "
                 "(id,age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,cardio)"
                 "values "
                 "({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});").format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        cursor.execute(query)
