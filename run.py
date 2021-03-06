from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(debug=True)


def hello_monkey():
    #Respond to incoming calls with a simple text message
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
