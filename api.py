from fastapi import FastAPI
from functions import *

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello'}

@app.get('/pit')
def PIT():
    pit()
    return {'message': 'pit triggered'}

@app.get('/flipper')
def FLIPPER():
    flipper()
    return {'message': 'flipper triggered'}

@app.get('/spinner')
def SPINNER():
    spinner(True)
    return {'message': 'spinner triggered'}


@app.get('/start')
def STARTMATCH():
    matchtimer()
    return {'message': 'match started'}