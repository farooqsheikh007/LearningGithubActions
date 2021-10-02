from flask import Flask

app = Flask(__name__)

@app.route("/")
def get():
    return '''
    <div style="margin: auto;right: 50%;bottom: 50%;transform: translate(50%,50%);position: absolute;"
    >
    <img src="https://c.tenor.com/fSsxftCb8w0AAAAi/pikachu-running.gif" alt="Computer man" style="width:48px;height:48px;">
    <p>Site is up and running</p>
    </div>
    '''

if(__name__ == '__main__'):
    app.run(host= "0.0.0.0", port=2090, debug= True)
