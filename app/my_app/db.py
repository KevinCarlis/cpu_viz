from flask import current_app
from flask import g
import mysql.connector
from mysql.connector import errorcode


#import os
#host = os.popen('ip route show | grep "default" | awk \'{print $3}\'').read().split('\n')[0]
#print(host)

def get_db():
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'db',
        'port': '3306',
        'database': 'cpudata'
    }
    try:
        if 'db' not in g:
            g.db = mysql.connector.connect(**config)
        return g.db
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)

