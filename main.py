from typing import List,Optional
from fastapi import FastAPI, Query
from model.dbHandler import match_exact, match_like
from fastapi.encoders import jsonable_encoder
app = FastAPI()


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instrucrion formaatted as JSON
    """
    response  = {"Usage is ":"/dict?word=<word>"}
    return jsonable_encoder(response)


@app.get("/dict")
def dictionary(words: List[str] = Query(None)):
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    if not words:
        response = {
            "status":"error",
            "word":words,
            "data":"word not found",
            }
        return jsonable_encoder(response)
    response = { "words" : []}
    for word in words:
        definitions = match_exact(word)
        if definitions:
            response["words"].append({"status":"success","word":word,"data":definitions})

        
        definitions = match_like(word)
        if definitions:
            response["words"].append({"status":"partial","word":word,"data":definitions})

        else:
            response["words"].append({"status":"error","word":word,"data":f"Word {word} not found in dict"})
            
    return jsonable_encoder(response)
    
