from flask import Blueprint, render_template, request, session
from my_app import regclass

bp = Blueprint("home", __name__)
registers = regclass.Registers()


@bp.route('/')
def home():
    registers.format('x')
    session['registers'] = registers.printable
    return render_template(
        'home/home.html',
        names=registers.names,
        pairs=registers.printable
    )


@bp.route('/', methods=['POST'])
def result():
    if request.method == 'POST':
        # result = request.form
        pairs = session.get('registers', None)
        return render_template(
            'home/home.html',
            names=registers.names,
            pairs=pairs
        )
