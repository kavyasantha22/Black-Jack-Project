# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the following code was made by myself
# using information on Python function usage
# from sources such as the official Python documentation,
# ChatGPT, and edX lessons
# Last access November, 2024

from objects import *
import sys
import os
import time
import functools

def summary(func):
    """
    Decorator that times the execution of the function 
    and prints the game summary after completion.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        player = func(*args, **kwargs)
        time_diff = time.perf_counter() - start_time
        print_game_summary(player, time_diff)
        return player
    return wrapper

def clear_terminal():
    """
    Clears the terminal screen based on the operating system.
    """
    if os.name == 'nt':
        os.system('cls')
        os.system('color')
    else:
        sys.stdout.write('\033c')
        sys.stdout.flush()

def get_name():
    """
    Prompts the user to input their name.
    """
    name = input("Please input your name: ")
    return name

def get_age(player_name):
    """
    Prompts the user to input their age and validates it.
    Exits the program if the user is under 18.
    """
    while True:
        age = input("Please input your age: ")
        try:
            age = int(age)
        except ValueError:
            print("\nAge must be a number!\n")
            continue
        if age > 120:
            print("\nI know you are not that old!\n")
            continue
        if age < 18:
            print(
                f"\n🚫 Sorry {player_name}, you need to wait {18 - age} more "
                "year(s) before playing (gambling). 🚫\n"
            )
            sys.exit(0)
        return age

def get_money():
    """
    Prompts the user to input the amount of money they will gamble with.
    Validates that the input is a positive number.
    """
    while True:
        money = input("💵 How much money are you gambling today? $")
        try:
            money = int(money)
            if money <= 0:
                print("\nAmount of money must be positive!\n")
                continue
            return money
        except ValueError:
            print("\nAmount of money must be numeric!\n")

def get_bet(player, round_count):
    """
    Prompts the player to input their bet for the current round.
    Validates that the bet is numeric and that the player has enough money.
    """
    while True:
        bet = input(f"💵 How much are you betting on round {round_count}? $")
        try:
            bet = int(bet)
        except ValueError:
            print("\nAmount of bet must be numeric!\n")
            continue
        if player.get_money() < bet:
            print("\nNot enough money...\n")
            continue
        if bet <= 0:
            print("\nBet must be a positive amount!\n")
            continue
        return bet

def choose_action(player, deck):
    """
    Prompts the player to choose an action: Hit, Double Down, or Stand.
    Executes the chosen action.
    """
    print("\nChoose your action:")
    print("1. Hit\n2. Double Down\n3. Stand")
    while True:
        chosen_action = input("👉 Input number: ")
        print()
        if chosen_action == "1":
            player.hit(deck)
            break
        elif chosen_action == "2":
            if player.double_down(deck) is None:
                print("\nNot enough money...\n")
                continue
            break
        elif chosen_action == "3":
            player.stand()
            break
        else:
            print("\nChoose appropriate action!\n")

def print_game_summary(player, time_diff):
    """
    Prints a summary of the game including total rounds played, time spent,
    and win rate.
    """
    player_summary = player.get_summary()
    final_money = player_summary["money_history"][-1]
    starting_money = player_summary["money_history"][0]
    total_rounds = player_summary["total_rounds"]

    if final_money > starting_money:
        end_statement = f"and managed to WIN ${final_money - starting_money}!!! 🎉"
    else:
        end_statement = "and managed to HAVE FUN!!! 🎲"

    minutes = int(time_diff // 60)
    seconds = int(time_diff % 60)

    print(
        f"🎉 You played {total_rounds} round(s) for {minutes} minutes "
        f"and {seconds} seconds, {end_statement}"
    )
    print(f"Win_rate: {player_summary['win_rate'] * 100:.2f}%")
    player_summary['plot']()
    print(f"Thank you {player_summary['name']} for playing!")
    print("See you next time! 👋")
    print("=" * 40)

@summary
def main():
    """
    Main function to run the Blackjack game.
    Sets up the game, handles game flow, and manages player actions.
    """
    # Initialize the game
    game = BlackJackGame()
    clear_terminal()
    print("=" * 40)
    print("🎲 WELCOME TO BLACKJACK 🎲".center(40))
    print("=" * 40)
    game.greet()
    print()

    # Get player information
    player_name = get_name()
    get_age(player_name)
    player_money = get_money()
    print("\n")
    if player_money >= 1000:
        print("💼 Ohohoho, we have an important guest here!", end="\n" * 3)
        time.sleep(1)
    game.set_up_player(player_name, player_money)
    print("✅ All set up! Ready to play.", end="\n" * 3)
    time.sleep(1)

    # Start game rounds
    round_count = 0
    while game.player.get_money() > 0:
        if round_count > 0:
            continue_game = input(
                "Do you want to continue the game? (Yes/No): "
            )
            if continue_game.lower() not in "yes":
                break
        clear_terminal()
        print(f"💰 Current Money: ${game.player.get_money()}")
        round_count += 1
        print("=" * 40)
        print(f"🎲 ROUND {round_count} 🎲".center(40))
        print("=" * 40)

        # Get player's bet for the round
        round_bet = get_bet(game.player, round_count)
        game.round_set_up(round_bet)

        # Player's turn
        while not game.player.is_busted() and game.player.playing:
            clear_terminal()
            print("=" * 40)
            print(f"🎲 ROUND {round_count} 🎲".center(40))
            print("=" * 40)
            print(f"Bet: {round_bet}")
            print("=" * 40)
            print()
            player_cards = game.get_player_card()
            dealer_cards = game.get_dealer_card()

            player_header = "🃏 Player's Cards"
            dealer_header = "🂠 Dealer's Cards"

            # Display player's and dealer's cards
            print(f"{player_header:<19} | {dealer_header:<20}")
            print("-" * 21 + "|" + "-" * 18)
            max_len = max(len(player_cards), len(dealer_cards))
            for i in range(max_len):
                player_card = player_cards[i] if i < len(player_cards) else " " * 20
                player_card = str(player_card)
                dealer_card = dealer_cards[i] if i < len(dealer_cards) else " " * 20
                dealer_card = str(dealer_card)
                if i == 1:
                    dealer_card = "*Hidden*"
                print(f"{player_card:<20} | {dealer_card:<20}")
            print("-" * 40)

            # Prompt player for action
            choose_action(game.player, game.deck)

        clear_terminal()
        print("=" * 40)
        print(f"🎲 ROUND {round_count} 🎲".center(40))
        print("=" * 40)

        # Check if player busted
        if game.player.is_busted():
            print("🃏 Final Player's Cards:")
            for card in game.player:
                print(f"  {card}")
            print(f"\nPlayer's value: {game.player.value}")
            print("\n💥 You Busted! 💥\n")
            game.player.lose()
            print("😞 You Lose... 😞\n")
            continue

        # Dealer's turn
        else:
            print("🃏 Final Player's Cards:")
            for card in game.player:
                print(f"  {card}")

            print(f"\nPlayer's value: {game.player.value}")
            print("\nDealer's Turn...", end="\n" * 2)
            time.sleep(1)
            game.dealer.play(game.deck)
            print("🂠 Dealer's Cards:")
            for card in game.dealer:
                print(f"  {card}")
                time.sleep(0.5)
            print(f"\nDealer's value: {game.dealer.value}")

        # Determine the outcome
        if game.dealer.is_busted():
            print("\n💥 Dealer Busted! 💥\n")
            game.player.win()
            print("🎉 YOU WIN!!! 🎉\n")
        elif game.get_winner() == game.player:
            game.player.win()
            print("\n🎉 YOU WIN!!! 🎉\n")
        else:
            game.player.lose()
            print("\n😞 You Lose... 😞\n")

    # End of the game
    if game.player.get_money() <= 0:
        print("Sorry, you don't have enough money left to gamble", end="\n" * 2)
        time.sleep(3)

    clear_terminal()
    return game.player

# Run the game
main()
