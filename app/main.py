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

from starlette.middleware.base import BaseHTTPMiddleware
import logging
from fastapi import Request

# Configure logging to include timestamp
logging.basicConfig(
    format='%(levelname)s> %(message)s',
    level=logging.INFO
)

class LogRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log request method and URL
        logging.info("<<<<<<<   Request   >>>>>>>")
        logging.info(f"Request URL: {request.url}")
        logging.info(f"Request Method: {request.method}")

        # Log headers
        logging.info("-------   Headers   -------")
        for name, value in request.headers.items():
            logging.info(f"{name}: {value}")
        logging.info("-------End of Headers-------")

        # Log body (if applicable)
        logging.info("-------   Body   -------")
        body = await request.body()
        logging.info(f"Request Body: {body.decode('utf-8')}")
        logging.info("-------End of Body-------")

        logging.info(">>>>>>>  End of Request   <<<<<<<")

        # Process the request
        response = await call_next(request)

        return response

# Add the middleware to the app
app.add_middleware(LogRequestMiddleware)

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
    logging.info(f"Received GET query parameters: '{query_params}'")
    return {"message": "Query parameters received", "query_params": dict(query_params)}


# POST endpoint
from datetime import datetime
@app.post("/")
async def root_print_post(request: Request):
    raw_body = await request.body()
    logging.info(f"Received POST raw body: '{raw_body.decode('utf-8')}'")

    body_content = raw_body.decode('utf-8')

    # Log the received raw body
    logging.info(f"Received POST raw body: '{body_content}'")

    # Create a unique filename using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = f"static/body_{timestamp}.txt"

    # Write the raw body to the file
    with open(filename, "w") as file:
        file.write(body_content)
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

