from flask import Flask
from Blueprint.graph_array import graph_array
from Blueprint.signal import signal

app = Flask(__name__)
app.register_blueprint(graph_array)
app.register_blueprint(signal)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
