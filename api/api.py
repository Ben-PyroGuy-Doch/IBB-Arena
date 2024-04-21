from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functions import *

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {'message': 'What you doing'}

@app.get('/pitup')
def PITUP():
    pitup()
    return {'message': 'Pit up'}

@app.get('/pitdown')
def PITDOWN():
    pitdown()
    return {'message': 'Pit down'}

@app.get('/flipper')
def FLIPPER():
    flipper()
    return {'message': 'Flipper triggered'}

@app.get('/spinner1c')
def SPINNER1C():
    spinner1c()
    return {'message': 'Spinner 1 Clockwise'}
    
@app.get('/spinner1a')
def SPINNER1A():
    spinner1a()
    return {'message': 'Spinner 1 Anti-Clockwise'}

@app.get('/spinner1off')
def SPINNER1OFF():
    spinner1off()
    return {'message': 'Spinner 1 Off'}

@app.get('/spinner2c')
def SPINNER2C():
    spinner2c()
    return {'message': 'Spinner 2 Clockwise'}

@app.get('/spinner2a')
def SPINNER2A():
    spinner2a()
    return {'message': 'Spinner 2 Anti-Clockwise'}
    
@app.get('/spinner2off')
def SPINNER2OFF():
    spinner2off()
    return {'message': 'Spinner 2 Off'}

@app.get('/spinner3c')
def SPINNER3C():
    spinner3c()
    return {'message': 'Spinner 3 Clockwise'}

@app.get('/spinner3a')
def SPINNER3A():
    spinner3a()
    return {'message': 'Spinner 3 Anti-Clockwise'}
    
@app.get('/spinner3off')
def SPINNER3OFF():
    spinner3off()
    return {'message': 'Spinner 3 Off'}

@app.get('/active')
def active():
    active()
    return {'active flag set'}

@app.get('/start120')
def STARTMATCH120():
    matchtimer120()
    return {'message': '2 min match started'}

@app.get('/start180')
def STARTMATCH180():
    matchtimer180()
    return {'message': '3 min match started'}

@app.get('/startduck')
def STARTMATCHDUCK():
    matchtimerDuck()
    return {'message': 'Duck match started'}

@app.get('/stop')
def STOPMATCH():
    stopmatch()
    return {'message': 'Match stop flag set'}