from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(
    prefix="/products",
    tags=["products"], 
    responses={404: {"message": "No Encontrado"}})

product_list = [{"id":1,"name":"producto1","description":"descripcion1","price":100}]

@router.get("/")
async def products():
    return product_list

@router.get("/{id}")
async def products(id: int):
    return product_list[id]