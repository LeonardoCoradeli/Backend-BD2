# app/api/v1/endpoints/CardController.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import UUID
from decimal import Decimal
from datetime import date
from app.services.CardService import CardsService,CardsThemeService,CardIntereactionService
from app.domain.CardModel import Card, CardTheme, CardInteraction
from app.core.config import get_cards_service, get_cards_theme_service, get_card_interaction_service

router = APIRouter()

# Cards Endpoints
@router.post("/cards/", response_model=Card, status_code=status.HTTP_201_CREATED)
async def create_card(card: Card, cards_service: CardsService = Depends(get_cards_service)):
    """
    Endpoint to create a new card.
    """
    try:
        return await cards_service.create(card)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/cards/{card_id}", response_model=Card)
async def get_card(card_id: UUID, cards_service: CardsService = Depends(get_cards_service)):
    """
    Endpoint to retrieve a card by ID.
    """
    card = await cards_service.get(card_id)
    if not card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found.")
    return card

@router.get("/cards/", response_model=List[Card])
async def list_cards(cards_service: CardsService = Depends(get_cards_service)):
    """
    Endpoint to list all cards.
    """
    return await cards_service.list()

@router.put("/cards/{card_id}", response_model=Card)
async def update_card(card_id: UUID, card: Card, cards_service: CardsService = Depends(get_cards_service)):
    """
    Endpoint to update a card's information.
    """
    try:
        return await cards_service.update(card_id, card)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/cards/{card_id}", response_model=Card)
async def delete_card(card_id: UUID, cards_service: CardsService = Depends(get_cards_service)):
    """
    Endpoint to delete a card by ID.
    """
    card = await cards_service.delete(card_id)
    if not card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found.")
    return card

# Cards Theme Endpoints
@router.post("/cards/themes/{theme_id}/add/{card_id}", status_code=status.HTTP_200_OK)
async def add_card_to_theme(theme_id: UUID, card_id: UUID, cards_theme_service: CardsThemeService = Depends(get_cards_theme_service)):
    """
    Endpoint to add a card to a theme.
    """
    try:
        await cards_theme_service.add_card_to_theme(card_id, theme_id)
        return {"message": "Card added to theme successfully."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/cards/themes/{theme_id}/remove/{card_id}", status_code=status.HTTP_200_OK)
async def remove_card_from_theme(theme_id: UUID, card_id: UUID, cards_theme_service: CardsThemeService = Depends(get_cards_theme_service)):
    """
    Endpoint to remove a card from a theme.
    """
    try:
        await cards_theme_service.remove_card_from_theme(card_id, theme_id)
        return {"message": "Card removed from theme successfully."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Card Interactions Endpoints
@router.post("/cards/interactions/", response_model=CardInteraction, status_code=status.HTTP_201_CREATED)
async def define_card_interaction(interaction: CardInteraction, card_interaction_service: CardIntereactionService = Depends(get_card_interaction_service)):
    """
    Endpoint to define an interaction between cards.
    """
    try:
        return await card_interaction_service.create(interaction)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/cards/{card_id}/interactions", response_model=List[CardInteraction])
async def get_card_interactions(card_id: UUID, card_interaction_service: CardIntereactionService = Depends(get_card_interaction_service)):
    """
    Endpoint to retrieve all interactions for a given card.
    """
    return await card_interaction_service.get_interactions_for_card(card_id)

# Price History Endpoints
@router.post("/cards/{card_id}/price", status_code=status.HTTP_200_OK)
async def record_card_price(
    card_id: UUID,
    price: Decimal,
    price_date: date,
    cards_service: CardsService = Depends(get_cards_service)
):
    """
    Endpoint to record a new price for a card.
    """
    try:
        await cards_service.record_card_price(card_id, price, price_date)
        return {"message": "Price recorded successfully."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/cards/{card_id}/latest-price", response_model=Decimal)
async def get_latest_card_price(
    card_id: UUID,
    cards_service: CardsService = Depends(get_cards_service)
):
    """
    Endpoint to retrieve the latest price of a card.
    """
    try:
        return await cards_service.get_latest_card_price(card_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/cards/{card_id}/price-history", response_model=List[dict])
async def get_card_price_history(
    card_id: UUID,
    cards_service: CardsService = Depends(get_cards_service)
):
    """
    Endpoint to retrieve the price history of a card.
    """
    try:
        price_history = await cards_service.get_price_history(card_id)
        return [{"price": record.price, "date": record.date} for record in price_history]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
