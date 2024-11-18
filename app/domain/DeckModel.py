from app.domain.BaseModel import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import date
from uuid import UUID

class Deck(BaseModel):
    id: UUID  # Primary identifier is a UUID
    user_id: UUID  # Changed from str to UUID
    name: str

class DeckCard(BaseModel):
    deck_id: UUID  # Changed from str to UUID
    card_id: UUID  # Changed from str to UUID
    quantity: Optional[int] = 1
    
class SynergyScore(BaseModel):
    deck_id: UUID  # Changed from str to UUID
    synergy_score: Decimal
    calculated_at: Optional[date] = None
