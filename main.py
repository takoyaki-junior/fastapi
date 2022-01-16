from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/country/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}


@app.get("/country/")
async def country(country_name: str = 'japan', country_no: int = 1):
    return {
        "country_name": country_name,
        "country_no": country_no
    }
