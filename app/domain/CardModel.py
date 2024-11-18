from decimal import Decimal
from datetime import date
from app.domain.BaseModel import BaseModel
from typing import Optional
from uuid import UUID

class Card(BaseModel):
    id: UUID  # Primary identifier is a UUID
    name: str
    _type: str
    mana_cost: int
    color: Optional[str] = None
    power: Optional[int] = None
    toughness: Optional[int] = None
    effect: Optional[str] = None
    _set: Optional[str] = None
    price: Optional[Decimal] = None

class CardTheme(BaseModel):
    card_id: UUID  # Changed to UUID
    theme: str

class CardInteraction(BaseModel):
    card_id_1: UUID  # Changed to UUID
    card_id_2: UUID  # Changed to UUID
    interaction_type: str

class PriceHistory(BaseModel):
    card_id: UUID  # Changed from str to UUID
    price: Decimal
    date: date