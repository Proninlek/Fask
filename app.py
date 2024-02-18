from flask import Flask, render_template, url_for, request, make_response, redirect

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)