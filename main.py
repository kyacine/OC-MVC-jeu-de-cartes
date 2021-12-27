"""Entry point."""

from models.card import Card
from models.deck import Deck
from models.player import Player

if __name__ == "__main__":
    card1 = Card("diamonds", "cinq")
    card2 = Card("coeurs", "cinq")
    card3 = Card("coeurs", "valet")
    print(card1 < card2)
    print(card3 > card2)

    deck = Deck()
    print(deck)

    player = Player("James")
    player.hand.append(deck.draw_card())
    print(player.hand)