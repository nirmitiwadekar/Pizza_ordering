import psycopg2
import psycopg2.extras

hostname = 'rohan'
database = 'pizza'
username = 'postgres'
pwd = '250201'
port_id = 5432
conn=None
cur=None
try:
    conn =psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
)

    cur=conn.cursor()

    create_script = '''CREATE TABLE IF NOT EXISTS pizza(
          pname varchar(20) NOT NULL,
          phone int NOT NULL,
          user varchar(10) NOT NULL,
          code varchar(20) NOT NULL 
        )'''

    cur.execute(create_script)

    conn.commit()
    
    
    
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
