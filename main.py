from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from routers import products,users


app = FastAPI()
app.title = "First API with FastAPI"
app.description = "API de Usuarios"
app.version = "0.0.1"

app.include_router(users.router)
app.include_router(products.router)