from flask import Flask, render_template, request, session, make_response
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = "1111111"


def Generate_seed():
    if random.randint(0, 10) % 2 == 0:
        return True
    else:
        return False


@app.route('/')
def hello_world():
    if Generate_seed():
        return render_template('height.html')
    else:
        return render_template('width.html')


@app.route('/cookie')
def cookie():
    resp = make_response(render_template("height.html"))
    resp.set_cookie("zhiyin", "你太美")
    session["zhiy"] = "666"
    print(request.cookies.get("zhiyin"))
    print(session.get("zhiy"))
    return resp


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True,)
