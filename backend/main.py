from flask import Flask, render_template, request
import psycopg2
import configparser
import os 


config = configparser.ConfigParser()
config.read("backend\config.ini")

app = Flask(__name__)


def get_db_conn():
    conn = psycopg2.connect(
        database= config.get('database', 'db_database'),
        user= config.get('database','db_user'),
        password= config.get('database', 'db_password'),
        host= config.get('database', 'db_host'),
        port= config.get('database', 'db_port')
    )
    return conn

@app.route('/')
def index():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('select * from cardinformation')
    cards = cur.fetchall()
    cur.close()
    conn.close()
    image_names = os.listdir(os.path.join(app.root_path, 'static', 'images'))

    selected_filter = request.args.get("filter")
    return render_template('index.html', cards=cards, selected_filter=selected_filter)




if __name__ == '__main__':
    app.run(debug=True)