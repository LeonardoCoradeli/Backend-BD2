from pydantic import BaseModel as PydanticBaseModel
from typing import Optional

class BaseModel(PydanticBaseModel):
    id: Optional[int] = None

    # Método para conversão para dicionário com `dict()`
    def dict(self, *args, **kwargs):
        # Inclui 'id' no dicionário apenas se estiver definido
        return super().dict(*args, exclude_unset=True, *args, **kwargs)
