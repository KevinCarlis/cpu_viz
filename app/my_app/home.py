from flask import Blueprint, render_template, request
from my_app import cpu


bp = Blueprint("home", __name__)
p = cpu.CPU()


@bp.get('/')
def home_get():
    return render_template(
        'home/home.html',
        pairs=p.registers(),
        instructions=p.instructions(),
        checked=0
    )


@bp.post('/')
def home_put():
    if 'encode' in request.form:
        """file1 = open("session.txt", "w")
        file1.write(', '.join(['{}={!r}'.format(k, v) for k, v
                    in request.form.items()]))
        file1.write('\n')
        file1.close()"""
        p.encode(**request.form)
    if 'run' in request.form:
        p.run(**request.form)
    return render_template(
        'home/home.html',
        pairs=p.registers(),
        instructions=p.instructions(),
        checked=int(request.form['inscheck'])
    )
