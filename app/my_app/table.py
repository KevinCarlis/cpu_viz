from flask import Blueprint, render_template, g

from my_app.db import get_db

bp = Blueprint("table", __name__)

@bp.route('/')
def table():
    db = get_db()
    cursor = db.cursor()
    query = ("SELECT * FROM registers")
    cursor.execute(query)
    #cursor=[['r0', '0']]
    return render_template('table/table.html', registers=cursor)

if __name__ == '__main__':
    app.run()

