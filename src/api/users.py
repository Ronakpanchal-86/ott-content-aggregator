from fastapi import APIRouter, status, HTTPException
from src.schemas.user import UserCreate, UserLogin
from src.services.user_service import (
    register_user,
    login_user,
    generate_login_token
)
router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    registered_user = register_user(user)

    if registered_user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already registered"
        )

    return registered_user


@router.post("/login")
def user_login(user: UserLogin):
    logged_in_user = login_user(user.email, user.password)

    if logged_in_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    return generate_login_token(logged_in_user)