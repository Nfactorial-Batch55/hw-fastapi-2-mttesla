from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.templating import Jinja2Templates

from .users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# (сюда писать решение)

@app.get('/users')
def get_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/{id}')
def get_id(id: int):
    user = next((user for user in users if user['id'] == id), None)
    if user is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return templates.TempateResponse('index.html', {'request': request, 'users': users})
# (конец решения)
