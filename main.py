"""This module is the entry point for neuralsymc api"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello There, Welcome to neural symc"}


@app.get("/neuralsymc")
async def neural_core():
    return {"message": "Hello, Am Neural Symc, How can I help you today?"}


@app.get("/api/v1/")
async def api_handler():
    return {"message": "hello There"}

