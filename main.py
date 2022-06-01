from flask import Flask, render_template
import os


app = Flask(__name__)


def main():
    app.run()


@app.route('/')
def face():
    return render_template('index_read.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
