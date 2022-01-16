from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/country/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}


@app.get("/country/")
async def country(country_name: str = 'japan', country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no
    }
