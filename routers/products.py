from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()

product_list = [{"id":1,"name":"producto1","description":"descripcion1","price":100}]

@router.get("/products")
async def products():
    return product_list