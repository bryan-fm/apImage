# app.py
from flask import Flask, request, jsonify
import random
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    response = {}
    response["MESSAGE"] = randomduck()
    return jsonify(response)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

def randomduck():
    patos = []
    patos.append("https://thumbs.dreamstime.com/z/um-pato-com-um-topete-63143800.jpg")
    patos.append("https://thumbs.dreamstime.com/z/um-pato-com-um-topete-63143800.jpg")
    patos.append("https://thumbs.dreamstime.com/z/pato-adornado-de-vibra%C3%A7%C3%A3o-1272298.jpg")
    patos.append("https://thumbs.dreamstime.com/z/bando-de-pato-tufado-mergulhador-branco-preto-com-olhos-amarelos-flutuando-em-lago-verde-na-%C3%A1ustria-europa-um-patos-tufados-156694258.jpg")
    patos.append("https://thumbs.dreamstime.com/z/pato-adornado-f%C3%AAmea-com-os-filhotes-no-lago-124599320.jpg")
    patos.append("https://thumbs.dreamstime.com/z/pato-masculino-do-pato-selvagem-96709436.jpg")
    patos.append("https://thumbs.dreamstime.com/z/pato-de-borracha-20347931.jpg")
    patos.append("https://thumbs.dreamstime.com/z/pato-selvagem-masculino-no-mar-b%C3%A1ltico-35389453.jpg")

    return random.choice(patos)
