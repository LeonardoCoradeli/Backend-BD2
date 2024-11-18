from app.services.BaseService import BaseService
from app.data.CardsRepository import CardsRepository,CardsThemeRepository,CardIntereactionRepository
from app.domain.CardModel import Card,CardTheme,CardInteraction
from app.services.BaseService import BaseService
from app.data.CardsRepository import PriceHistoryRepository
from app.domain.CardModel import PriceHistory
from typing import Optional, List
from uuid import UUID
from decimal import Decimal
from datetime import date
class CardsService(BaseService[Card]):
    def __init__(self, repository: CardsRepository):
        super().__init__(repository)

    async def get_cards_by_theme(self, theme_id: int) -> List[Card]:
        """
        Retrieve all cards associated with a specific theme.
        """
        return await self.repository.get_cards_by_theme(theme_id)

    async def filter_cards(self, mana_cost: Optional[int] = None, card_type: Optional[str] = None) -> List[Card]:
        """
        Filter cards by optional parameters like mana cost or card type.
        """
        return await self.repository.filter_cards(mana_cost=mana_cost, card_type=card_type)

    async def calculate_card_value(self, card_id: int) -> float:
        """
        Calculate the value of a card based on its interactions and other metrics.
        """
        card = await self.get(card_id)
        if not card:
            raise ValueError(f"Card with ID {card_id} not found.")
        
        interactions = await self.repository.get_card_interactions(card_id)
        # Implement your custom logic to evaluate card value based on interactions
        return sum(interaction.effectiveness_score for interaction in interactions)

class CardsThemeService(BaseService[CardTheme]):
    def __init__(self, repository: CardsThemeRepository):
        super().__init__(repository)

    async def add_card_to_theme(self, card_id: int, theme_id: int):
        """
        Add a card to a specified theme.
        """
        await self.repository.add_card_to_theme(card_id, theme_id)

    async def remove_card_from_theme(self, card_id: int, theme_id: int):
        """
        Remove a card from a specified theme.
        """
        await self.repository.remove_card_from_theme(card_id, theme_id)

    async def analyze_deck_synergy(self, deck_id: int) -> float:
        """
        Analyze the thematic synergy score of all cards in a deck.
        """
        cards = await self.repository.get_deck_cards(deck_id)
        # Implement your custom logic for synergy calculation based on themes
        return self._calculate_synergy_score(cards)

    def _calculate_synergy_score(self, cards: List[Card]) -> float:
        """
        Placeholder method for calculating synergy score.
        """
        # Example logic, replace with actual calculations
        return sum(card.synergy_weight for card in cards)

        
class CardIntereactionService(BaseService[CardInteraction]):
    def __init__(self, repository: CardIntereactionRepository):
        super().__init__(repository)

    async def define_interaction(self, card_id: int, related_card_id: int, effectiveness_score: float):
        """
        Define a new interaction between two cards with a given effectiveness score.
        """
        await self.repository.create_interaction(card_id, related_card_id, effectiveness_score)

    async def get_interactions_for_card(self, card_id: int) -> List[CardInteraction]:
        """
        Retrieve all interactions for a given card.
        """
        return await self.repository.get_interactions_for_card(card_id)

    async def evaluate_interaction_strength(self, card_id: int) -> float:
        """
        Evaluate the total strength of interactions for a card.
        """
        interactions = await self.get_interactions_for_card(card_id)
        # Example logic to evaluate total strength
        return sum(interaction.effectiveness_score for interaction in interactions)

class PriceService(BaseService[PriceHistory]):
    def __init__(self, repository: PriceHistoryRepository):
        super().__init__(repository)

    async def record_price(self, card_id: UUID, price: Decimal, date: date):
        """
        Record a new price for a card.
        """
        await self.repository.add_price_record(card_id, price, date)

    async def get_latest_price(self, card_id: UUID) -> PriceHistory:
        """
        Retrieve the latest price for a specific card.
        """
        return await self.repository.get_latest_price(card_id)

    async def get_price_history(self, card_id: UUID) -> List[PriceHistory]:
        """
        Retrieve the price history for a specific card.
        """
        return await self.repository.get_price_history(card_id)
