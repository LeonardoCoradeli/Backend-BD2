from typing import TypeVar, Generic, List, Optional
from app.data.BaseRepository import BaseRepository
from app.domain.BaseModel import BaseModel

T = TypeVar('T', bound=BaseModel)

class BaseService(Generic[T]):
    def __init__(self, repository):
        self.repository = repository

    async def create(self, obj: T) -> T:
        return await self.repository.create(obj)

    async def get(self, obj_id: int) -> Optional[T]:
        return await self.repository.get(obj_id)

    async def list(self) -> List[T]:
        return await self.repository.list()

    async def update(self, obj_id: int, obj: T) -> T:
        return await self.repository.update(obj_id, obj)

    async def delete(self, obj_id: int) -> Optional[T]:
        return await self.repository.delete(obj_id)
