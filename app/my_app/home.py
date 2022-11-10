from flask import Blueprint, render_template, request, session
from my_app import regclass


bp = Blueprint("home", __name__)
registers = regclass.Registers()
instructions = regclass.Instructions()
#cpu = cpu.CPU()


@bp.route('/')
def home():
    session['registers'] = registers()
    return render_template(
        'home/home.html',
        names=registers.get_names(),
        pairs=session.get('registers', None),
        instructions=instructions()
    )


@bp.route('/', methods=['POST'])
def result():
    if request.method == 'POST':
        file1 = open("session.txt", "w")
#        for item in request.form:
        file1.write(', '.join(['{}={!r}'.format(k,v) for k,v in request.form.items()]))
        file1.close()
        
        pairs = session.get('registers', None)
        return render_template(
            'home/home.html',
            names=registers.get_names(),
            pairs=pairs,
            instructions=instructions()
        )
