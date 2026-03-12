import psycopg2


def get_connection():

    conn = psycopg2.connect(
        host="localhost",
        database="aryana_ai_db",
        user="postgres",
        password="Naysa",
        port="5432"
    )

    return conn