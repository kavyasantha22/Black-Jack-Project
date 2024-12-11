# Blackjack Game in Python/Java 🃏

This is an object-oriented implementation of the classic **Blackjack** card game in two vesion, Python and Java. The project simulates a single-player game against a dealer, featuring game logic, betting mechanics, and statistics tracking. The code integrates user-friendly features, clear terminal UI, and data visualization for an engaging experience.

---

## Features 🎮

- **Card and Deck Management**:
  - Standard 52-card deck with shuffle and reshuffle mechanics.
  - Cards dynamically generated and managed using Python/Java's OOP.

- **Game Mechanics**:
  - Traditional Blackjack rules:
    - Aces count as 1 or 11 depending on the hand's value.
    - Dealer draws until their hand value is at least 17.
  - Player actions:
    - **Hit**
    - **Stand**
    - **Double Down**
  - Bust checking and hand adjustments for Aces.
  - Clear terminal displays for each game round.

- **Betting System**:
  - Players can place bets and double down.
  - Tracks the player's money and bet history.
  - Handles cases for insufficient money to place bets or double down.

- **Statistics and Visualization**:
  - Tracks wins, losses, and win rate.
  - Visualizes money history using `matplotlib`.
  - Provides a detailed game summary at the end, including time spent and financial performance.

- **Interactive Gameplay**:
  - User-friendly prompts for actions such as age verification, name input, and betting.
  - Detailed display of cards for both player and dealer.
  - Automatic reshuffling when the deck is exhausted.

- **Object-Oriented Design**:
  - Modular classes (`Card`, `Deck`, `Player`, `Dealer`, etc.) for easy customization and extension.

---

## How to Play 🎲

1. **Setup**:
   - Run the program and follow the prompts to input your name, age, and starting money.
   - A shuffled deck is initialized for each game.

2. **Gameplay**:
   - Place a bet at the start of each round.
   - Decide to:
     - **Hit**: Take another card.
     - **Stand**: End your turn.
     - **Double Down**: Double your bet and take one more card.
   - Try to beat the dealer's hand without exceeding 21.

3. **Outcome**:
   - The program automatically determines whether the player wins, loses, or the dealer busts.
   - A detailed summary of the game, including financial performance and win rate, is shown at the end.

---

## Code Highlights 📂

### Python

- **`main.py`**:
  - Handles the game flow and user interactions.
  - Includes helper functions for clearing the terminal, getting user input, and managing game rounds.
  - Implements a `summary` decorator to track game duration and display a final summary.

- **`objects.py`**:
  - Core logic for the game, including card management, betting mechanics, and game rules.

- **Functions in `main.py`**:
  - `get_name`, `get_age`, and `get_money`: Collect and validate player input.
  - `get_bet`: Ensures valid bets within the player's budget.
  - `choose_action`: Guides the player through their turn.
  - `print_game_summary`: Displays a final summary with gameplay stats and a plot of money history.
  - `main`: Orchestrates the game logic, including player and dealer turns, round management, and game conclusion.

### Java
## Code Structure 📂

- **`Player.java`**:
  - Inherits from `Person` and manages player-specific attributes and actions:
    - Money management.
    - Betting logic.
    - Actions like `hit`, `stand`, and `doubleDown`.
  - Implements game-related methods:
    - `placeBet(int betAmount)`: Places a valid bet if the player has enough money.
    - `lose()`: Deducts the bet amount from the player's money on a loss.
    - `win()`: Adds the bet amount to the player's money on a win.

- **`Deck.java`**:
  - Manages deck creation, shuffling, and dealing of cards.

- **`Card.java`**:
  - Represents individual cards with suits, ranks, and values.

- **`Person.java`**:
  - Base class for both `Player` and `Dealer`.
  - Handles card management and hand value calculations.

- **`Main.java`**:
  - Contains the main game loop:
    - Initializes players and the deck.
    - Manages rounds, including betting, player actions, and dealer logic.
    - Displays outcomes and tracks statistics.

---
