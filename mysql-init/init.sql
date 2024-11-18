-- Tabela de usuários
CREATE TABLE Users (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de cartas
CREATE TABLE Cards (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    name VARCHAR(100) NOT NULL,
    _type VARCHAR(50) NOT NULL,
    mana_cost INT NOT NULL,
    color VARCHAR(20),
    power INT,
    toughness INT,
    effect TEXT,
    _set VARCHAR(50),  -- 'set' é palavra reservada em MySQL, coloquei entre crases
    price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de decks
CREATE TABLE Decks (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    user_id CHAR(36) NOT NULL,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Tabela de relação entre decks e cartas
CREATE TABLE Deck_Cards (
    deck_id CHAR(36) NOT NULL,
    card_id CHAR(36) NOT NULL,
    quantity INT DEFAULT 1,
    PRIMARY KEY (deck_id, card_id),
    FOREIGN KEY (deck_id) REFERENCES Decks(id) ON DELETE CASCADE,
    FOREIGN KEY (card_id) REFERENCES Cards(id) ON DELETE CASCADE
);

-- Tabela de temas das cartas
CREATE TABLE Card_Themes (
    id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    card_id CHAR(36) NOT NULL,
    theme VARCHAR(50) NOT NULL,
    FOREIGN KEY (card_id) REFERENCES Cards(id) ON DELETE CASCADE
);

-- Tabela de interações entre cartas
CREATE TABLE Card_Interactions (
    card_id_1 CHAR(36) NOT NULL,
    card_id_2 CHAR(36) NOT NULL,
    interaction_type VARCHAR(50) NOT NULL,
    PRIMARY KEY (card_id_1, card_id_2),
    FOREIGN KEY (card_id_1) REFERENCES Cards(id) ON DELETE CASCADE,
    FOREIGN KEY (card_id_2) REFERENCES Cards(id) ON DELETE CASCADE
);

-- Tabela de histórico de preços das cartas
CREATE TABLE Price_History (
    card_id CHAR(36) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY (card_id, date),
    FOREIGN KEY (card_id) REFERENCES Cards(id) ON DELETE CASCADE
);

-- Tabela de pontuações de sinergia
CREATE TABLE Synergy_Scores (
    deck_id CHAR(36) NOT NULL,
    synergy_score DECIMAL(5, 2) NOT NULL,
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (deck_id, calculated_at),
    FOREIGN KEY (deck_id) REFERENCES Decks(id) ON DELETE CASCADE
);
