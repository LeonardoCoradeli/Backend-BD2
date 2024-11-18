from app.services.UserService import UserService
from app.data.UserRepository import UserRepository
from app.services.CardService import CardsService, CardsThemeService, CardIntereactionService, PriceService
from app.data.CardsRepository import CardsRepository, CardsThemeRepository, CardIntereactionRepository, PriceHistoryRepository
from app.services.DeckService import DeckService, DeckCardsService, SynergyScoresService
from app.data.DeckRepository import DecksRepository, DeckCardsRepository, SynergyScoresRepository
from databases import Database

DATABASE_URL = "mysql+aiomysql://user:password@localhost:3305/Banco"

# Initialize database connection (assuming async Database object)
database = Database(DATABASE_URL)

# Dependency Injection for UserService
async def get_user_service() -> UserService:
    user_repository = UserRepository()
    return UserService(user_repository)

# Dependency Injection for CardsService
async def get_cards_service() -> CardsService:
    cards_repository = CardsRepository()
    price_history_repository = PriceHistoryRepository()
    price_service = PriceService(price_history_repository)
    return CardsService(cards_repository)

# Dependency Injection for CardsThemeService
async def get_cards_theme_service() -> CardsThemeService:
    cards_theme_repository = CardsThemeRepository()
    return CardsThemeService(cards_theme_repository)

# Dependency Injection for CardIntereactionService
async def get_card_interaction_service() -> CardIntereactionService:
    card_interaction_repository = CardIntereactionRepository()
    return CardIntereactionService(card_interaction_repository)

# Dependency Injection for PriceService
async def get_price_service() -> PriceService:
    price_history_repository = PriceHistoryRepository()
    return PriceService(price_history_repository)

# Dependency Injection for DeckService
async def get_deck_service() -> DeckService:
    decks_repository = DecksRepository()
    return DeckService(decks_repository)

# Dependency Injection for DeckCardsService
async def get_deck_cards_service() -> DeckCardsService:
    deck_cards_repository = DeckCardsRepository()
    return DeckCardsService(deck_cards_repository)

# Dependency Injection for SynergyScoresService
async def get_synergy_scores_service() -> SynergyScoresService:
    synergy_scores_repository = SynergyScoresRepository()
    return SynergyScoresService(synergy_scores_repository)
