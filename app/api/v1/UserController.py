# app/api/v1/endpoints/UserController.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import UUID
from app.services.UserService import UserService
from app.domain.UserModel import User
from app.core.config import get_user_service
from pydantic import BaseModel

router = APIRouter()

class UserUpdateRequest(BaseModel):
    """
    Pydantic model for user update request.
    This model can be extended based on your User model requirements.
    """
    name: str
    email: str
    is_active: bool

@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User, user_service: UserService = Depends(get_user_service)):
    """
    Endpoint to create a new user.
    """
    try:
        return await user_service.create(user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: UUID, user_service: UserService = Depends(get_user_service)):
    """
    Endpoint to retrieve a user by ID.
    """
    user = await user_service.get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return user

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: UUID, user_data: UserUpdateRequest, user_service: UserService = Depends(get_user_service)):
    """
    Endpoint to update user data.
    """
    try:
        return await user_service.update_user(user_id, user_data.dict())
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: UUID, user_service: UserService = Depends(get_user_service)):
    """
    Endpoint to delete a user by ID.
    """
    user = await user_service.delete(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return user

@router.get("/users/email/{email}", response_model=User)
async def get_user_by_email(email: str, user_service: UserService = Depends(get_user_service)):
    """
    Endpoint to retrieve a user by email.
    """
    try:
        return await user_service.get_by_email(email)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/users/active", response_model=List[User])
async def list_active_users(user_service: UserService = Depends(get_user_service)):
    """
    Endpoint to list active users.
    """
    try:
        return await user_service.list_active_users()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
