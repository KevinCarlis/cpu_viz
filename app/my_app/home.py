from flask import Blueprint, render_template, request, session
from my_app import regclass

bp = Blueprint("home", __name__)
registers = regclass.Registers()
instructions = regclass.Instructions()


@bp.route('/')
def home():
    session['registers'] = registers()
    return render_template(
        'home/home.html',
        names=registers.get_names(),
        pairs=registers(),
        instructions=instructions()
    )


@bp.route('/', methods=['POST'])
def result():
    if request.method == 'POST':
        # result = request.form
        pairs = session.get('registers', None)
        return render_template(
            'home/home.html',
            names=registers.get_names(),
            pairs=pairs
        )
