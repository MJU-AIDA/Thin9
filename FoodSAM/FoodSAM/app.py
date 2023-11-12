import os
from fastapi import FastAPI
from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import shutil

from FoodSAM.panoptic import panoptic


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check")
def root():
    return {"Hello": "World"}

@app.post("/img_seg_to_json")
def img_seg_to_json(file: bytes = File(...), output_dir: str):

    return panoptic(file, output_dir)

