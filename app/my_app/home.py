from flask import Blueprint, render_template, url_for, request

bp = Blueprint("home", __name__)

@bp.route('/')
def home():
    return render_template('home/home.html', registers=[
        ["R0","00000000"],
        ["R1","00000000"],
        ["R2","00000000"],
        ["R3","00000000"],
        ["R4","00000000"],
        ["R5","00000000"],
        ["PC","00000000"],
        ["CPSR","00000000"]
    ])

@bp.route('/', methods=['POST'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('home/home.html')

if __name__ == '__main__':
    app.run()

