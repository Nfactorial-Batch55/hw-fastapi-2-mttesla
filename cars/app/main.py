from fastapi import FastAPI, Response, Query, HTTPException
from typing import List

from .cars import create_cars

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()


@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")


# (сюда писать решение)
@app.get('/cars')
def get_cars(page: int = Query(1, alias='page'), limit: int = Query(10, alias='limit')):
    start = (page - 1) * limit
    end = start + limit
    return cars[start:end]


@app.get('/cars/{id}')
def get_id(id: int):
    for car in cars:
        if car['id'] == id:
            return car
    raise HTTPException(status_code=404, detail='Item not found')
    

# (конец решения)
