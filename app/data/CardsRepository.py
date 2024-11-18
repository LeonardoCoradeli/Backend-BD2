from app.data.BaseRepository import BaseRepository
from app.domain.CardModel import Card, CardTheme, CardInteraction
from uuid import UUID
from typing import List
from databases import Database
from app.domain.CardModel import PriceHistory
from decimal import Decimal
from datetime import date

class CardsRepository(BaseRepository[Card]):
    def __init__(self):
        super().__init__("Cards", Card)

    async def get_cards_by_name(self, name: str) -> List[Card]:
        """
        Retrieve cards by name (exact or partial match).
        """
        query = f"SELECT * FROM {self.table_name} WHERE name LIKE :name"
        rows = await self.database.fetch_all(query=query, values={"name": f"%{name}%"})
        return [self.model(**row) for row in rows]

    async def get_cards_by_mana_cost(self, mana_cost: int) -> List[Card]:
        """
        Retrieve cards by mana cost.
        """
        query = f"SELECT * FROM {self.table_name} WHERE mana_cost = :mana_cost"
        rows = await self.database.fetch_all(query=query, values={"mana_cost": mana_cost})
        return [self.model(**row) for row in rows]

class CardsThemeRepository(BaseRepository[CardTheme]):
    def __init__(self):
        super().__init__("Card_Themes", CardTheme)

    async def add_card_to_theme(self, card_id: UUID, theme: str):
        """
        Add a card to a specified theme.
        """
        query = f"INSERT INTO {self.table_name} (card_id, theme) VALUES (:card_id, :theme)"
        await self.database.execute(query=query, values={"card_id": card_id, "theme": theme})

    async def remove_card_from_theme(self, card_id: UUID, theme: str):
        """
        Remove a card from a specified theme.
        """
        query = f"DELETE FROM {self.table_name} WHERE card_id = :card_id AND theme = :theme"
        await self.database.execute(query=query, values={"card_id": card_id, "theme": theme})

class CardIntereactionRepository(BaseRepository[CardInteraction]):
    def __init__(self):
        super().__init__("Card_Interactions", CardInteraction)

    async def create_interaction(self, card_id_1: UUID, card_id_2: UUID, interaction_type: str):
        """
        Define a new interaction between two cards.
        """
        query = f"INSERT INTO {self.table_name} (card_id_1, card_id_2, interaction_type) VALUES (:card_id_1, :card_id_2, :interaction_type)"
        await self.database.execute(query=query, values={"card_id_1": card_id_1, "card_id_2": card_id_2, "interaction_type": interaction_type})

    async def get_interactions_for_card(self, card_id: UUID) -> List[CardInteraction]:
        """
        Retrieve all interactions for a given card.
        """
        query = f"SELECT * FROM {self.table_name} WHERE card_id_1 = :card_id OR card_id_2 = :card_id"
        rows = await self.database.fetch_all(query=query, values={"card_id": card_id})
        return [self.model(**row) for row in rows]


class PriceHistoryRepository(BaseRepository[PriceHistory]):
    def __init__(self):
        super().__init__("Price_History", PriceHistory)

    async def get_latest_price(self, card_id: UUID) -> PriceHistory:
        """
        Retrieve the most recent price record for a specific card.
        """
        query = f"SELECT * FROM {self.table_name} WHERE card_id = :card_id ORDER BY date DESC LIMIT 1"
        row = await self.database.fetch_one(query=query, values={"card_id": card_id})
        return self.model(**row) if row else None

    async def get_price_history(self, card_id: UUID) -> List[PriceHistory]:
        """
        Retrieve the entire price history for a specific card.
        """
        query = f"SELECT * FROM {self.table_name} WHERE card_id = :card_id ORDER BY date DESC"
        rows = await self.database.fetch_all(query=query, values={"card_id": card_id})
        return [self.model(**row) for row in rows]

    async def add_price_record(self, card_id: UUID, price: Decimal, date: date):
        """
        Add a new price record for a specific card.
        """
        query = f"INSERT INTO {self.table_name} (card_id, price, date) VALUES (:card_id, :price, :date)"
        await self.database.execute(query=query, values={"card_id": card_id, "price": price, "date": date})