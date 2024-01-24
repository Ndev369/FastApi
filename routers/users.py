from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()

class User(BaseModel):
    id: int 
    name: str
    surname: str
    url: str
    age: int
    
    
    
user_list = [User(id=1,name = "julio",surname = "gomez",url = "google.com",age =21),
        User(id=2,name ="jose",surname="perez",url="google.com",age = 32),
        User(id=3,name = "rafa",surname = "rodriguez",url = "google.com",age = 44)]
    


@router.get("/usersjson")
async def userjson():
    return [{ "name":"brias","surname":"moure","url":"https://www.google.com","age":23}]


@router.get("/users")
async def users():
    return user_list

#PATH
@router.get("/user/{id}") 
async def user(id: int):
   return search_user(id)


#QUERY
@router.get("/user") 
async def user(id: int):
    return search_user(id)
    
    
@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404,detail="El usuario ya existe")
    else:
        user_list.append(user)
        return {"ok":"Usuario agregado correctamente"}
    
@router.put("/user/")
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    if not found:
        raise HTTPException(status_code=404,detail="El usuario no existe")
   
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
    if not found:
        return {"Error":"No se ha eliminado el usuario"}
    else:
        return {"ok":"Usuario eliminado correctamente"}




def search_user(id:int):
    users = filter(lambda user: user.id == id,user_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el Usuario"}
    