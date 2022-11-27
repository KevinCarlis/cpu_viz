from flask import Blueprint, render_template, request, session
from my_app import parts, cpu


bp = Blueprint("home", __name__)
p = cpu.CPU()
r = parts.Registers()
i = parts.Instructions()

@bp.route('/')
def home():
    return render_template(
        'home/home.html',
        pairs=r.registers(),
        instructions=i.instructions()
    )


@bp.route('/', methods=['POST'])
def result():
    if request.method == 'POST':
        if 'encode' in request.form:
            file1 = open("session.txt", "w")
            file1.write(', '.join(['{}={!r}'.format(k,v) for k,v in request.form.items()]))
            file1.write('\n')
            file1.close()
        
        return render_template(
            'home/home.html',
            pairs=r.registers(),
            instructions=i.instructions()
        )
