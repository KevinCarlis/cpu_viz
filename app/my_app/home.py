from flask import Blueprint, render_template, url_for, request, session

bp = Blueprint("home", __name__)


@bp.route('/')
def home():
    registers = [
        ["R0", "00000000"],
        ["R1", "00000000"],
        ["R2", "00000000"], 
        ["R3", "00000000"],
        ["R4", "00000000"],
        ["R5", "00000000"],
        ["PC", "00000000"],
        ["CPSR", "0000000"]
    ]
    session['registers'] = registers
    return render_template('home/home.html',
                            **locals()
                            )

@bp.route('/', methods=['POST'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('home/home.html', 
                                registers = session.get('registers', None)
                                )

if __name__ == '__main__':
    app.run()

