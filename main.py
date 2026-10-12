from fastapi import FastAPI
from searching import bfs_search, dfs_search, hill_climbing_search

app = FastAPI()

# Tareas -metodos
#create -post
#read-get
#update -put
#delete -delete

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/bfs")
def bfs_search(item: dict):
    resultado = bfs_search()
    return {"item": "Aqui se implementara la busqueda BFS"}

@app.post("/dfs")
def dfs_search(item: dict):
    resultado = dfs_search()
    return {"item": "Aqui se implementara la busqueda DFS"}

@app.post("/hill-climbing")
def hill_climbing_search(item: dict):
    resultado = hill_climbing_search()
    return {"item": "Aqui se implementara la busqueda de escalada"}
