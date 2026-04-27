import sqlite3

def create_connection(db_name="sales.db"):
    return sqlite3.connect(db_name)

def save_to_db(df, conn):
    df.to_sql("sales", conn, if_exists="replace", index=False)