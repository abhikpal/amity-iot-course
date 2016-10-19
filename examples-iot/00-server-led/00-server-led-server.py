from flask import Flask, redirect

app = Flask(__name__)

led_state = 0

@app.route('/')
def index():
    return str(led_state)

@app.route('/set/')
def state_changer():
    return """
    <!DOCTYPE HTML>
    <html>
    <head>
        <title>Server LED</title>
        <style>
        body    { width: 45em; margin:auto; margin-top: 2em; }
        a       { text-decoration: none; color:white;
                  font-weight: bold; font-size:3em; }
        div     { min-width: 30em; margin:auto; padding:5em; background:rgb(187, 187, 187); }
        .on     { background: rgb(241, 101, 41); }
        .off    { background: rgb(96, 144, 255); }
        </style>
    </head>
    <body>
        <div class="on"><a href="/set/1/">ON</a></div>
        <br>
        <div class="off"><a href="/set/0/">OFF</a></div>
    </body>
    </html>
    """

@app.route('/set/<state>/')
def chnage_state(state):
    global led_state
    led_state = int(state)
    return redirect('/set/')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
