from app.services.BaseService import BaseService
from app.data.DeckRepository import DeckCardsRepository,DecksRepository,SynergyScoresRepository
from app.domain.DeckModel import Deck,DeckCard,SynergyScore
from uuid import UUID
from typing import List
from decimal import Decimal



class DeckService(BaseService[Deck]):
    def __init__(self, repository: DecksRepository):
        super().__init__(repository)

    async def create_deck_for_user(self, user_id: UUID, name: str) -> Deck:
        """
        Create a new deck for a specific user.
        """
        deck = Deck(user_id=user_id, name=name)
        return await self.create(deck)

    async def get_decks_by_user(self, user_id: UUID) -> List[Deck]:
        """
        Retrieve all decks for a specific user.
        """
        return await self.repository.get_decks_by_user(user_id)


class DeckCardsService(BaseService[DeckCard]):
    def __init__(self, repository: DeckCardsRepository):
        super().__init__(repository)

    async def add_card_to_deck(self, deck_id: UUID, card_id: UUID, quantity: int = 1):
        """
        Add a card to a specific deck. If it already exists, update the quantity.
        """
        await self.repository.add_card_to_deck(deck_id, card_id, quantity)

    async def remove_card_from_deck(self, deck_id: UUID, card_id: UUID):
        """
        Remove a card from a specific deck.
        """
        await self.repository.remove_card_from_deck(deck_id, card_id)

    async def get_cards_in_deck(self, deck_id: UUID) -> List[DeckCard]:
        """
        Retrieve all cards in a specified deck.
        """
        return await self.repository.get_cards_in_deck(deck_id)

        
class SynergyScoresService(BaseService[SynergyScore]):
    def __init__(self, repository: SynergyScoresRepository):
        super().__init__(repository)

    async def calculate_synergy_score(self, deck_id: UUID) -> SynergyScore:
        """
        Calculate and store the synergy score for a given deck.
        """
        # Example placeholder logic to retrieve deck cards and calculate synergy
        deck_cards = await self.repository.get_cards_in_deck(deck_id)
        score = self._calculate_score(deck_cards)
        synergy_score = SynergyScore(deck_id=deck_id, synergy_score=score)
        return await self.create(synergy_score)

    def _calculate_score(self, deck_cards: List[DeckCard]) -> Decimal:
        """
        Placeholder method for calculating synergy score based on deck cards.
        """
        # Replace with your actual logic for synergy calculation
        return Decimal(len(deck_cards))  # Example: simple count of cards
