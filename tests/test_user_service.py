import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services.UserService import UserService
from app.domain.user import User
from app.data.UserRepository import UserRepository

@pytest.fixture
def mock_repository():
    # Cria um mock para o UserRepository com métodos assíncronos
    mock_repo = AsyncMock(spec=UserRepository)
    return mock_repo

@pytest.fixture
def user_service(mock_repository):
    # Usa o mock do repositório para inicializar o UserService
    return UserService(mock_repository)

@pytest.mark.asyncio
async def test_create_user(user_service, mock_repository):
    # Dados de exemplo
    user = User(name="John Doe", email="johndoe@example.com")
    mock_repository.create.return_value = 1  # Simula retorno de ID

    # Chama o método create do UserService
    user_id = await user_service.create(user)

    # Verifica se o repositório foi chamado com o usuário correto
    mock_repository.create.assert_called_once_with(user)
    assert user_id == 1

@pytest.mark.asyncio
async def test_get_user(user_service, mock_repository):
    # Configura o mock para retornar um objeto User
    user = User(id=1, name="John Doe", email="johndoe@example.com")
    mock_repository.get.return_value = user

    # Chama o método get do UserService
    result = await user_service.get(1)

    # Verifica se o repositório foi chamado corretamente
    mock_repository.get.assert_called_once_with(1)
    assert result == user

@pytest.mark.asyncio
async def test_list_users(user_service, mock_repository):
    # Configura o mock para retornar uma lista de usuários
    users = [User(id=1, name="John Doe", email="johndoe@example.com")]
    mock_repository.list.return_value = users

    # Chama o método list do UserService
    result = await user_service.list()

    # Verifica se o repositório foi chamado corretamente
    mock_repository.list.assert_called_once()
    assert result == users

@pytest.mark.asyncio
async def test_update_user(user_service, mock_repository):
    # Dados de exemplo
    user = User(name="John Doe", email="johndoe@example.com")

    # Chama o método update do UserService
    await user_service.update(1, user)

    # Verifica se o repositório foi chamado com os parâmetros corretos
    mock_repository.update.assert_called_once_with(1, user)

@pytest.mark.asyncio
async def test_delete_user(user_service, mock_repository):
    # Chama o método delete do UserService
    await user_service.delete(1)

    # Verifica se o repositório foi chamado com o ID correto
    mock_repository.delete.assert_called_once_with(1)
