from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/members')
def about():
    return render_template('members.html')


if __name__ == '__main__':
    app.run()
