from library import *

app = Flask(__name__)

socketio = SocketIO(app)


@app.route("/")
def interface():
    return render_template(
        "interface.html",
    )

if __name__ == "__main__":
    serve(app, host='172.16.54.10', port=80)
