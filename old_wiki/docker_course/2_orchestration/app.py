
from flask import Flask
import mariadb
import sys



app = Flask(__name__)

def get_num_visits(conn):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(visit_time) FROM log;")
    return int(cur.fetchone()[0])

def update_visits(conn):
    cur = conn.cursor()
    try:
        print(f"trying insert", file=sys.stderr)
        cur.execute("INSERT INTO `log` (`visit_time`) VALUES (now());")
    except mariadb.Error as e: 
        print(f"Error: {e}", file=sys.stderr)


def get_last_visit(conn):
    cur = conn.cursor()
    cur.execute("SELECT visit_time FROM log ORDER BY visit_time DESC LIMIT 1;")
    return cur.fetchone()[0]



def get_db_data():
    try:
        conn = mariadb.connect(user="root", password="root", host="db", port=3306, database="testdb")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return "oopsie :)"
    
    conn.autocommit = True


    num_visits = get_num_visits(conn)
    update_visits(conn)

    print('Hello world!', file=sys.stderr)
    

    if num_visits > 0:
        last_visit = get_last_visit(conn)
        conn.close()

        return f"Ich wurde {num_visits} mal aufgerufen bis jetzt.\nDer letzte Besuch war: {last_visit}"
    else:
        conn.close()

        return f"Ich wurde {num_visits} mal aufgerufen bis jetzt.\nDu bist also der erste Besucher :)"

            

@app.route('/')
def hello():
    count = get_db_data()
    return 'Daten aus der Datenbank:\n{}\n'.format(count)




