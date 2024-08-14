from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import HTTPException


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.mount(
    "/home",
    StaticFiles(directory="home", html=True),
    name="home",
)


@app.get("/")
async def landingpage():
    response = RedirectResponse(url="/home")
    return response


@app.get("/status")
async def root():
    """
    Method to check status of server
    """
    try:
        return {"code": 1, "detail": "online"}
    except:
        raise HTTPException(status_code=404, detail="offline")

################################################
### Custom endpoint for door opening service ###
################################################
import requests

DOOR_MAP = {
    "main": "http://172.17.0.77/3I_O.htm?R=Pulse+Door+Open+First+Door",
    "1": "http://172.17.0.78/3I_O.htm?R=Pulse+Door+Open+First+Door",
    "2": "http://172.17.0.79/3I_O.htm?R=Pulse+Door+Open+First+Door",
}


@app.get("/open-door/{door_id}")
def call_url(door_id: str):
    """Open the `main`, `1` or `2` door."""
    url = DOOR_MAP.get(door_id)
    response = requests.get(url)
    return {"status_code": response.status_code, "content": response.text}

