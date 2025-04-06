import random

values = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        for suit in suits:
            for rank in values:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards: list[Card] = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "A":
            self.aces += 1

        # Make the ace worth 1 instead of 11 when applicable
        while self.value > 21 and self.aces:
            # Ace is worth an 11 - so 11 - 10 = 1
            # (Ace's alternate value if you bust)
            self.value -= 10
            # set ace to zero
            # (as if you don't have one
            # - but in actuality the ace is set to one)
            self.aces -= 1

    def __str__(self):  # magical method (overrides default print() behavior)
        return ", ".join(str(card) for card in self.cards)


def play_blackjack():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # First two cards
    for _ in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    print("Dealer's show card:", dealer_hand.cards[0])
    print("Your hand:", player_hand)
    print("Your total:", player_hand.value)

    # Player's turn
    while player_hand.value < 21:
        action = input("Hit or stand? ").lower()
        if action == "hit":
            player_hand.add_card(deck.deal_card())
            print("Your hand:", player_hand)
            print("Your total:", player_hand.value)
        elif action == "stand":
            break
        else:
            print("Invalid input.")

    if player_hand.value > 21:
        print("Bust! Dealer wins.")
        return

    # Dealer's turn
    print("Dealer's hand:", dealer_hand)
    while dealer_hand.value < 17:
        dealer_hand.add_card(deck.deal_card())
        print("Dealer hits:", dealer_hand)

    print("Dealer's total:", dealer_hand.value)

    # Compare point totals
    if dealer_hand.value > 21 or player_hand.value > dealer_hand.value:
        print("You win!")
    elif dealer_hand.value == player_hand.value:
        print("It's a tie!")
    else:
        print("Dealer wins.")


if __name__ == "__main__":
    play_blackjack()
