# app/services/UserService.py
from app.services.BaseService import BaseService
from app.data.UserRepository import UserRepository
from app.domain.UserModel import User
from typing import Optional, List
from pydantic import ValidationError
from fastapi import HTTPException, status

class UserService(BaseService[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)

    async def create(self, user: User) -> User:
        """
        Create a new user with validation and optional logic for setting default values.
        """
        # Custom validation example
        if await self.repository.get_by_email(user.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this email already exists."
            )

        # Additional logic (e.g., hashing password if applicable)
        user.password = self._hash_password(user.password)
        
        # Create user using the base service's create method
        return await super().create(user)

    async def get_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by their email.
        """
        user = await self.repository.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )
        return user

    async def update_user(self, user_id: int, user_data: dict) -> User:
        """
        Update user data with validation and integrity checks.
        """
        existing_user = await self.get(user_id)
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )

        # Update only allowed fields
        for key, value in user_data.items():
            if hasattr(existing_user, key):
                setattr(existing_user, key, value)

        # Save the updated user
        return await self.repository.update(user_id, existing_user)

    def _hash_password(self, password: str) -> str:
        """
        Placeholder method for password hashing (implement using a secure method).
        """
        # Example logic; replace with actual hashing logic such as bcrypt
        return "hashed_" + password

    # Example additional logic (optional)
    async def list_active_users(self) -> List[User]:
        """
        Retrieve a list of active users only.
        """
        return await self.repository.list_active_users()
