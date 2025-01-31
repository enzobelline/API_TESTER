from fastapi import APIRouter, Depends
from API_TESTER.core.security import verify_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    return {"message": "Access granted", "user": payload["sub"]}
