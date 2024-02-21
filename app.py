from flask import Flask, render_template, url_for, request, make_response, redirect
from moduls import db

app = Flask(__name__)
app.config['SECRET_KEY'] = b''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
moduls.db.init_app(app)


@app.cli.commands('init-db')
def init_db():
    moduls.db.creat_all()
    print('OK')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cloth/')
def cloth():
    return render_template('cloth.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')


@app.route('/form/')
def form():
    return render_template('form.html')


@app.route('/save/', methods=['POST'])
def save():
    name = request.form.get('name')
    email = request.form.get('email')
    resp = make_response(redirect('/welcome'))
    resp.set_cookie('name', name)
    resp.set_cookie('email', email)
    return resp


@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    if name:
        return render_template('welcome.html', name=name)
    else:
        return redirect('/form/')


@app.route('/logout', methods=['POST'])
def logout():
    resp = make_response(redirect('/form/'))
    resp.delete_cookie('name')
    resp.delete_cookie('email')
    return resp


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        last_name = request.form['Имя']
        first_name = request.form['Фамилия']
        email = register.form['Email']
        password = generate_password_hash(request.form['Пароль'])

        new_user = moduls.User(last_name=last_name, first_name=first_name, email=email, password=password)
        moduls.db.session.add(new_user)
        moduls.db.session.commit()

        return redirect('/welcome.html/')


    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)