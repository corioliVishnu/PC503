#!/bin/python3

import random
import time

# Slot Machine Game
class SlotMachine:
    def __init__(self):
        # Define the slot machine symbols and payouts
        self.symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '🔔', '💎']
        self.payouts = {
            '🍒': 2,
            '🍋': 3,
            '🍊': 5,
            '🍉': 10,
            '⭐': 20,
            '🔔': 50,
            '💎': 100
        }
        self.balance = 1000  # Start with a balance of 1000
        self.bet_amount = 10  # Default bet amount
    
    def spin_reels(self):
        """Simulate spinning the three reels."""
        reel1 = random.choice(self.symbols)
        reel2 = random.choice(self.symbols)
        reel3 = random.choice(self.symbols)
        return reel1, reel2, reel3

    def check_win(self, spin_result):
        """Check if the player wins based on the spin result."""
        if spin_result[0] == spin_result[1] == spin_result[2]:
            symbol = spin_result[0]
            payout = self.payouts.get(symbol, 0)
            return True, payout
        else:
            return False, 0

    def play_round(self):
        """Play a round of the slot machine game."""
        print("\nSpinning the reels...")
        time.sleep(1)  # Simulate the delay of spinning

        # Spin the reels
        spin_result = self.spin_reels()
        print(f"Reels: {spin_result[0]} | {spin_result[1]} | {spin_result[2]}")

        # Check if the player has won
        win, payout = self.check_win(spin_result)
        if win:
            print(f"You win! Payout: {payout} credits")
            self.balance += payout
        else:
            print("No win this time. Better luck next time!")

    def display_balance(self):
        """Display the current balance."""
        print(f"\nCurrent balance: {self.balance} credits")

    def set_bet(self):
        """Allow the player to set the bet amount."""
        while True:
            try:
                bet = int(input(f"Enter your bet amount (Current balance: {self.balance}): "))
                if bet <= 0:
                    print("Bet must be a positive number.")
                elif bet > self.balance:
                    print("Insufficient balance! Please enter a smaller amount.")
                else:
                    self.bet_amount = bet
                    break
            except ValueError:
                print("Invalid input! Please enter a number.")

    def play(self):
        """Main game loop."""
        print("\nWelcome to the Casino Slot Machine Game!")
        while self.balance > 0:
            self.display_balance()

            # Ask if the player wants to play or quit
            choice = input("\nDo you want to play a round? (y/n): ").lower()
            if choice == 'n':
                print(f"\nThanks for playing! Your final balance is: {self.balance} credits.")
                break
            elif choice == 'y':
                self.set_bet()
                self.play_round()
            else:
                print("Invalid choice. Please choose 'y' or 'n'.")
        else:
            print("\nYou are out of credits! Game over.")

# Main function to run the game
if __name__ == "__main__":
    # Create a SlotMachine object
    slot_machine = SlotMachine()
    
    # Start the game
    slot_machine.play()

