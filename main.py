from flask import Flask, render_template


app = Flask(__name__)


def main():
    app.run()


@app.route('/')
def face():
    return render_template('index_read.html')


if __name__ == '__main__':
    main()