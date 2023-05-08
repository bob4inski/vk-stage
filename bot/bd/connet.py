from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
import os
load_dotenv()


def get_pg_connection():
    pg_conn = psycopg2.connect(host=os.getenv('DATABASE_HOST') or '127.0.0.1', port=os.getenv('DATABASE_PORT'),
                               database=os.getenv('DATABASE_NAME'), user=os.getenv('DATABASE_USER'),
                               password=os.getenv('DATABASE_PASSWORD'), cursor_factory=RealDictCursor)
    pg_conn.autocommit = True
    return pg_conn

