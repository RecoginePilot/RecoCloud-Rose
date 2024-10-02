from fastapi.responses import RedirectResponse, FileResponse
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

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")

# @app.get("/")
# async def landingpage():
#     response = RedirectResponse(url="/home")
#     return response

from fastapi import Request
@app.get("/")
def root_print_get(request: Request):
    query_params = request.query_params
    print(f"Received GET query parameters: {query_params}")
    return {"message": "Query parameters received", "query_params": dict(query_params)}


# POST endpoint
@app.post("/")
async def root_print_post(request: Request):
    raw_body = await request.body()
    print(f"Received POST raw body: {raw_body.decode('utf-8')}")
    return {"message": "Raw body received", "raw_body": raw_body.decode("utf-8")}




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
    if url is None:
        return {"status_code": 404, "content": "Invalid door_id"}
    response = requests.get(url)
    return {"status_code": response.status_code, "content": response.text}

