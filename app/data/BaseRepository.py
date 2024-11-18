from typing import TypeVar, Generic, List, Optional, Type
from app.domain.BaseModel import BaseModel
from databases import Database

T = TypeVar('T', bound=BaseModel)

class BaseRepository(Generic[T]):
    database: Database  # Banco de dados padrão compartilhado para todas as instâncias

    def __init__(self, table_name: str, model: Type[T]):
        self.table_name = table_name
        self.model = model

    async def create(self, obj: T) -> T:
        query = f"INSERT INTO {self.table_name} ({', '.join(obj.dict().keys())}) VALUES ({', '.join([':' + key for key in obj.dict().keys()])})"
        values = obj.dict()
        insert_id = await self.database.execute(query=query, values=values)
        return await self.get(insert_id)

    async def get(self, obj_id: int) -> Optional[T]:
        query = f"SELECT * FROM {self.table_name} WHERE id = :id"
        row = await self.database.fetch_one(query=query, values={"id": obj_id})
        return self.model(**row) if row else None

    async def list(self) -> List[T]:
        query = f"SELECT * FROM {self.table_name}"
        rows = await self.database.fetch_all(query=query)
        return [self.model(**row) for row in rows]

    async def update(self, obj_id: int, obj: T) -> Optional[T]:
        query = f"UPDATE {self.table_name} SET {', '.join([f'{key} = :{key}' for key in obj.dict().keys()])} WHERE id = :id"
        values = {**obj.dict(), "id": obj_id}
        await self.database.execute(query=query, values=values)
        return await self.get(obj_id)

    async def delete(self, obj_id: int) -> Optional[T]:
        obj = await self.get(obj_id)
        if obj:
            query = f"DELETE FROM {self.table_name} WHERE id = :id"
            await self.database.execute(query=query, values={"id": obj_id})
        return obj
