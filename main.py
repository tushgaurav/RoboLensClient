# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import threading
from helpers import program1, program2
# import robot


class Pose(BaseModel):
    name: str
    id: int


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    print("Starting up")
    # thread = threading.Thread(target=robot.powerOn)
    #
    # t = threading.Thread(target=runP1)
    # t.start()


@app.get("/")
async def root():
    return {"message": "Robot Powering On"}


@app.post("/pose/")
async def pose1(pose: Pose):

    # thread.start()
    poseId = pose.id
    print(poseId)
    if poseId < 0 or poseId > 5:
        # Invalid poseId
        return {"message": "Invalid Pose, must be between 0 and 5"}

    if poseId == 0:
        # Pose 0

        thread = threading.Thread(target=program1)
        thread.start()

        return {"message": "Pose 0 - Started"}

    if poseId == 1:
        # Pose 1
        return {"message": "Pose 1 - Started"}

    if poseId == 2:
        # Pose 2
        return {"message": "Pose 2 - Started"}

    if poseId == 3:
        # Pose 3
        return {"message": "Pose 3 - Started"}


@app.get("/status")
async def status():
    # thread = threading.Thread(target=robot.powerOn)
    # thread.start()
    return {"message": "Robot is running"}


@app.post("/poweroff")
async def poweroff():
    # thread = threading.Thread(target=robot.powerOff)
    # thread.start()
    return {"message": "Powering Off"}
