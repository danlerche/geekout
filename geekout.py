from flask import Flask, abort, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def geekout():
    our_title = 'Geek Out'
    return render_template('geekout.html', title=our_title)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug='true')














