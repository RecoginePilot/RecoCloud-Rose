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
