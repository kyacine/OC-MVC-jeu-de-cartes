"""Entry point."""

from controllers.base import Controller
from models.deck import Deck
from views.base import View


def main():
    deck = Deck()
    view = View()
    game = Controller(deck, view)
    game.run()

if __name__ == '__main__':
    main()


# if __name__ == "__main__":
#     card1 = Card("diamonds", "cinq")
#     card2 = Card("coeurs", "cinq")
#     card3 = Card("coeurs", "valet")
#     print(card1 < card2)
#     print(card3 > card2)
#
#     deck = Deck()
#     print(deck)
#
#     player = Player("James")
#     player.hand.append(deck.draw_card())
#     print(player.hand)