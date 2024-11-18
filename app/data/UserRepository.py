# app/data/UserRepository.py
from app.data.BaseRepository import BaseRepository
from app.domain.UserModel import User
from typing import Optional, List

class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(table_name="users", model=User)

    async def get_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by their email.
        """
        query = f"SELECT * FROM {self.table_name} WHERE email = :email"
        row = await self.database.fetch_one(query=query, values={"email": email})
        return self.model(**row) if row else None

    async def list_active_users(self) -> List[User]:
        """
        List all active users.
        """
        query = f"SELECT * FROM {self.table_name} WHERE active = true"
        rows = await self.database.fetch_all(query=query)
        return [self.model(**row) for row in rows]
