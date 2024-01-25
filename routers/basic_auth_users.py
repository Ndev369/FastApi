from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
app.title = "Authentication API"
app.version = "0.0.1"
oauth2 = OAuth2PasswordBearer(tokenUrl="/login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
    
class UserDB(User):
    password: str

users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "john@gmail.com",
        "disabled": False,
        "password": "123456"
},
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@gmail.com",
        "disabled": True,
        "password": "12345"
        }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales invalidas",
            headers={"WWW-Authenticate": "Bearer"})
        
    if user.disabled:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo",
            headers={"WWW-Authenticate": "Bearer"})
    return user
@app.post("/login", tags=["Login"])
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, 
            detail="Usuario no es correcto")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, 
            detail="Contraseña incorrecta")
    
    return {"access_token": user.username, "token_type": "bearer"}
 
 
@app.get("/users/me", tags=["Get users"])
async def me(user: User = Depends(current_user)):
    return user