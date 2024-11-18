# app/api/v1/endpoints/DeckController.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import UUID
from app.services.DeckService import DeckService, DeckCardsService, SynergyScoresService
from app.domain.DeckModel import Deck, DeckCard, SynergyScore
from app.core.config import get_deck_service, get_deck_cards_service, get_synergy_scores_service

router = APIRouter()

# Deck Endpoints
@router.post("/decks/", response_model=Deck, status_code=status.HTTP_201_CREATED)
async def create_deck(user_id: UUID, name: str, deck_service: DeckService = Depends(get_deck_service)):
    """
    Endpoint to create a new deck for a user.
    """
    try:
        return await deck_service.create_deck_for_user(user_id, name)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/decks/user/{user_id}", response_model=List[Deck])
async def get_user_decks(user_id: UUID, deck_service: DeckService = Depends(get_deck_service)):
    """
    Endpoint to retrieve all decks for a specific user.
    """
    try:
        return await deck_service.get_decks_by_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/decks/{deck_id}", response_model=Deck)
async def delete_deck(deck_id: UUID, deck_service: DeckService = Depends(get_deck_service)):
    """
    Endpoint to delete a specific deck.
    """
    try:
        deck = await deck_service.delete(deck_id)
        if not deck:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deck not found.")
        return deck
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Deck Cards Endpoints
@router.post("/decks/{deck_id}/cards/", status_code=status.HTTP_200_OK)
async def add_card_to_deck(deck_id: UUID, card_id: UUID, quantity: int = 1, deck_cards_service: DeckCardsService = Depends(get_deck_cards_service)):
    """
    Endpoint to add a card to a specified deck.
    """
    if quantity < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quantity must be at least 1.")
    try:
        await deck_cards_service.add_card_to_deck(deck_id, card_id, quantity)
        return {"message": "Card added to deck successfully."}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/decks/{deck_id}/cards/{card_id}", status_code=status.HTTP_200_OK)
async def remove_card_from_deck(deck_id: UUID, card_id: UUID, deck_cards_service: DeckCardsService = Depends(get_deck_cards_service)):
    """
    Endpoint to remove a card from a specified deck.
    """
    try:
        await deck_cards_service.remove_card_from_deck(deck_id, card_id)
        return {"message": "Card removed from deck successfully."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/decks/{deck_id}/cards", response_model=List[DeckCard])
async def get_deck_cards(deck_id: UUID, deck_cards_service: DeckCardsService = Depends(get_deck_cards_service)):
    """
    Endpoint to retrieve all cards in a specified deck.
    """
    try:
        return await deck_cards_service.get_cards_in_deck(deck_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Synergy Scores Endpoints
@router.post("/decks/{deck_id}/synergy-score", response_model=SynergyScore, status_code=status.HTTP_201_CREATED)
async def calculate_synergy_score(deck_id: UUID, synergy_scores_service: SynergyScoresService = Depends(get_synergy_scores_service)):
    """
    Endpoint to calculate and store the synergy score for a specified deck.
    """
    try:
        return await synergy_scores_service.calculate_synergy_score(deck_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
