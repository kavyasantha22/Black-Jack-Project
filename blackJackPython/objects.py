# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the following code was made by myself
# using information on Python function usage
# from sources such as the official Python documentation,
# ChatGPT, and edX lessons
# Last access November, 2024

import numpy as np  
import matplotlib.pyplot as plt

class Card:
    """Represents a playing card with a suit and rank."""

    # Class variable using dictionary comprehension
    rank_values = {str(n): n for n in range(2, 11)}
    rank_values.update({rank: 10 for rank in ['Jack', 'Queen', 'King']})
    rank_values['Ace'] = 11

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        self._value = self.calculate_value()

    def calculate_value(self):
        """Calculates the numerical value of the card."""
        try:
            return self.rank_values[self._rank]
        except KeyError:
            raise ValueError(f"Card rank '{self._rank}' is not defined!")

    @property
    def value(self):
        """Returns the value of the card."""
        return self._value

    @property
    def rank(self):
        """Returns the rank of the card."""
        return self._rank

    @property
    def suit(self):
        """Returns the suit of the card."""
        return self._suit

    def __str__(self):
        """Special method for string representation."""
        return f"{self._rank} of {self._suit}"

    def __repr__(self):
        """Special method for official string representation."""
        return f"Card('{self._suit}', '{self._rank}')"

class Deck:
    """Represents a deck of 52 playing cards."""

    def __init__(self):
        self._suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self._ranks = [
            '2', '3', '4', '5', '6', '7', '8', '9', '10',
            'Jack', 'Queen', 'King', 'Ace'
        ]
        self._index = 0
        self.deck_generator = self.set_up()

    def set_up(self):
        """Initializes and shuffles the deck using a generator."""
        cards = [Card(suit, rank) for suit in self._suits for rank in self._ranks]
        np.random.shuffle(cards)
        for card in cards:
            yield card  # Generator yielding cards one at a time

    def deal_card(self):
        """Deals a card from the deck; reshuffles if the deck is empty."""
        try:
            self._index += 1
            return next(self.deck_generator)
        except StopIteration:
            print("Deck is empty. Reshuffling...")
            self.deck_generator = self.set_up()
            self._index = 1
            return next(self.deck_generator)

    def __len__(self):
        """Returns the number of remaining cards in the deck."""
        return 52 - self._index

class Person:
    """Base class for Player and Dealer."""

    def __init__(self, name):
        self.name = name
        self._cards = []
        self._value = 0
        self._hard_aces = 0  # Aces counted as 11
        self._busted = False

    def set_up(self, deck):
        """Deals two initial cards to the person."""
        self._value = 0
        self._hard_aces = 0
        self._busted = False
        self._cards = []
        for _ in range(2):
            self.add_card(deck.deal_card())

    @property
    def cards(self):
        """Returns the list of cards in hand."""
        return self._cards

    @property
    def value(self):
        """Returns the total value of the hand."""
        return self._value

    @property
    def hard_aces(self):
        """Returns the number of aces counted as 11."""
        return self._hard_aces

    def add_card(self, card):
        """Adds a card to the hand and adjusts for aces if necessary."""
        self._cards.append(card)
        self._value += card.value
        if card.rank == "Ace":
            self._hard_aces += 1
        self.adjust_for_ace()
        self.check_busted()

    def check_busted(self):
        """Checks if the hand value exceeds 21."""
        self._busted = self._value > 21

    def adjust_for_ace(self):
        """Adjusts aces from 11 to 1 if hand value exceeds 21."""
        while self._value > 21 and self._hard_aces > 0:
            self._value -= 10
            self._hard_aces -= 1

    def empty_cards(self):
        """Clears the hand of cards."""
        self._cards = []

    def is_busted(self):
        """Returns True if the hand value exceeds 21."""
        return self._busted

    def __iter__(self):
        """Allows iteration over the person's cards."""
        return iter(self._cards)

def playing_checker(method):
    """Decorator to check if the player is still playing before proceeding."""

    def wrapper(self, *args, **kwargs):
        if self.playing:
            return method(self, *args, **kwargs)
        else:
            print(f"{self.name} is no longer playing.")
            return None
    return wrapper

class Player(Person):
    """Represents the player in the game, inherits from Person."""

    def __init__(self, name, money):
        super().__init__(name)
        self.money = money
        self.current_bet = None
        self.playing = True
        self.game_stats = GameStats(money)

    @playing_checker  # Using a decorator to check if player can perform action
    def hit(self, deck):
        """Player takes another card."""
        new_card = deck.deal_card()
        self.add_card(new_card)

    def stand(self):
        """Player decides to stop taking cards."""
        self.playing = False

    @playing_checker # Using a decorator to check if player can perform action
    def double_down(self, deck):
        """Player doubles the bet and takes exactly one more card."""
        if 2 * self.current_bet > self.money:
            return None
        else:
            self.current_bet *= 2
            self.hit(deck)
            self.stand()
            return 1

    def place_bet(self, bet_amount):
        """Places a bet for the current round."""
        if bet_amount > self.money:
            print("Not enough money...")
            return None
        else:
            self.current_bet = bet_amount
            return 1

    def player_playing(self, status):
        """Sets the player's playing status."""
        self.playing = status

    def get_status(self):
        """Returns the player's playing status."""
        return self.playing

    def lose(self):
        """Handles the scenario when the player loses."""
        self.game_stats.record_round(0, self.current_bet)
        self.money -= self.current_bet

    def win(self):
        """Handles the scenario when the player wins."""
        self.game_stats.record_round(1, self.current_bet)
        self.money += self.current_bet

    def get_money(self):
        """Returns the player's current money."""
        return self.money

    def get_summary(self):
        """Returns a summary of the player's game statistics."""
        player_summary = self.game_stats.summary()
        player_summary['name'] = self.name
        return player_summary

class Dealer(Person):
    """Represents the dealer in the game, inherits from Person."""

    def __init__(self, name):
        super().__init__(name)

    def play(self, deck):
        """Dealer draws cards until the hand value is at least 17."""
        while self.value < 17:
            self.add_card(deck.deal_card())

class BlackJackGame:
    """Manages the flow of the Blackjack game."""

    def __init__(self):
        self.dealer = Dealer("Pablo")
        self.player = None
        self.deck = None
        self.set_up_deck()

    def greet(self):
        """Displays a welcome message."""
        print("Welcome to Black Jack Game managed by Pablo")

    def set_up_player(self, player_name, player_money):
        """Initializes the player."""
        self.player = Player(player_name, player_money)

    def set_up_deck(self):
        """Initializes and shuffles the deck."""
        self.deck = Deck()
        self.deck.set_up()

    def round_set_up(self, round_bet):
        """Prepares the game for a new round."""
        self.set_up_deck()
        self.player.set_up(self.deck)
        self.dealer.set_up(self.deck)
        self.player.playing = True
        self.player.current_bet = round_bet

    def get_player_card(self):
        """Returns the player's cards."""
        return self.player.cards

    def get_dealer_card(self):
        """Returns the dealer's cards."""
        return self.dealer.cards

    def get_winner(self):
        """Determines the winner of the round."""
        if self.player.value > self.dealer.value:
            return self.player
        else:
            return self.dealer

class GameStats:
    """Tracks the game statistics for the player using NumPy."""

    def __init__(self, starting_money):
        """Use NumPy array to store values to ease stat calculation"""
        self._outcomes = np.array([])  
        self._bet_history = np.array([])
        self._money_history = np.array([starting_money])

    def record_round(self, outcome, round_bet):
        """Records the outcome and bet amount of a round."""
        self._outcomes = np.append(self._outcomes, outcome)
        self._bet_history = np.append(self._bet_history, round_bet)
        new_money = (
            self._money_history[-1] + round_bet if outcome
            else self._money_history[-1] - round_bet
        )
        self._money_history = np.append(self._money_history, new_money)

    def get_win_rate(self):
        """Calculates the win rate of the player."""
        if self._outcomes.size == 0:
            return 0
        return np.mean(self._outcomes)

    def plot_money_history(self):
        """Plots the player's money history over the rounds."""
        if self._money_history.size <= 1:
            print("Not enough data to plot money history.")
            return
        plt.figure(figsize=(10, 6))
        plt.plot(self._money_history, marker='o', linestyle='-', color='b')
        plt.title("Money History Over Rounds")
        plt.xlabel("Round")
        plt.ylabel("Money")
        plt.grid(True)
        plt.show()

    def summary(self):
        """Provides a summary of the player's game statistics."""
        summary_dict = {
            key.lstrip('_'): value for key, value in self.__dict__.items()
        }
        summary_dict['total_rounds'] = len(self._outcomes)
        summary_dict['wins'] = int(np.sum(self._outcomes))
        summary_dict['losses'] = len(self._outcomes) - summary_dict['wins']
        summary_dict['plot'] = self.plot_money_history
        summary_dict['win_rate'] = self.get_win_rate()
        return summary_dict
