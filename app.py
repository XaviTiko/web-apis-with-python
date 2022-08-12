# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {"usage": "/dict?=<word>"}
    # Since this is a website with front-end, we don't need to send the usage instructions
    return jsonify(response)


@app.get("/dict")
def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    words = request.args.getlist("word")
    
    if not words:
        return jsonify({"status":"ERROR","word":words,"data":"Word not found"})
    response = { "words" : []}
    for word in words:
        definition = match_exact(word)
        if definition:
            response["words"].append( {"status":"all to well","word is ":word,"Data":definition})
        else:
            definition = match_like(word)
            if definition:
                response["words"].append( {"status":"something not clear","word is ":word,"Data":definition})
            else:
                response["words"].append({"status":"ERROR","word":words,"data":"no definition"})
    
    return jsonify(response)


if __name__ == "__main__":
    app.run()
