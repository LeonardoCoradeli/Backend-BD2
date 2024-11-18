# app/data/DeckRepository.py
from app.data.BaseRepository import BaseRepository
from app.domain.DeckModel import Deck, DeckCard, SynergyScore
from typing import List
from uuid import UUID

class DecksRepository(BaseRepository[Deck]):
    def __init__(self):
        super().__init__("Decks", Deck)

    async def get_decks_by_user(self, user_id: UUID) -> List[Deck]:
        query = f"SELECT * FROM {self.table_name} WHERE user_id = :user_id"
        rows = await self.database.fetch_all(query=query, values={"user_id": user_id})
        return [self.model(**row) for row in rows]

class DeckCardsRepository(BaseRepository[DeckCard]):
    def __init__(self):
        super().__init__("Deck_Cards", DeckCard)

    async def add_card_to_deck(self, deck_id: UUID, card_id: UUID, quantity: int):
        query = f"SELECT * FROM {self.table_name} WHERE deck_id = :deck_id AND card_id = :card_id"
        existing_card = await self.database.fetch_one(query=query, values={"deck_id": deck_id, "card_id": card_id})
        if existing_card:
            update_query = f"UPDATE {self.table_name} SET quantity = quantity + :quantity WHERE deck_id = :deck_id AND card_id = :card_id"
            await self.database.execute(query=update_query, values={"deck_id": deck_id, "card_id": card_id, "quantity": quantity})
        else:
            insert_query = f"INSERT INTO {self.table_name} (deck_id, card_id, quantity) VALUES (:deck_id, :card_id, :quantity)"
            await self.database.execute(query=insert_query, values={"deck_id": deck_id, "card_id": card_id, "quantity": quantity})

    async def remove_card_from_deck(self, deck_id: UUID, card_id: UUID):
        query = f"DELETE FROM {self.table_name} WHERE deck_id = :deck_id AND card_id = :card_id"
        await self.database.execute(query=query, values={"deck_id": deck_id, "card_id": card_id})

    async def get_cards_in_deck(self, deck_id: UUID) -> List[DeckCard]:
        query = f"SELECT * FROM {self.table_name} WHERE deck_id = :deck_id"
        rows = await self.database.fetch_all(query=query, values={"deck_id": deck_id})
        return [self.model(**row) for row in rows]

class SynergyScoresRepository(BaseRepository[SynergyScore]):
    def __init__(self):
        super().__init__("Synergy_Scores", SynergyScore)

    async def get_synergy_score(self, deck_id: UUID) -> SynergyScore:
        query = f"SELECT * FROM {self.table_name} WHERE deck_id = :deck_id ORDER BY calculated_at DESC LIMIT 1"
        row = await self.database.fetch_one(query=query, values={"deck_id": deck_id})
        return self.model(**row) if row else None
