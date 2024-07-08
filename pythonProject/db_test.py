from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


engine = create_engine("postgresql+psycopg2://jip_user:jip_password@localhost:5432/jip_database")
connection = engine.connect()
print("Подключение к SQLAlchemy установлено")

connection.close()

connection = psycopg2.connect(user="jip_user", password="jip_password", dbname="jip_database")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()

cursor.execute("SELECT 1")
result = cursor.fetchone()
print("Результат запроса с помощью psycopg2:", result)

cursor.close()
connection.close()
print("Соединение с помощью psycopg2 закрыто")