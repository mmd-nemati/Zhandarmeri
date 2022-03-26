import card
import clue

all_wall_cards = []

class WallCard(card.Card):
    
    def __init__(self, given_clues):
        self.wall_clues = []
        global all_wall_cards
        for i in given_clues:
            locals()[i] = clue.Clue(i)
            self.wall_clues.append(locals()[i])
        all_wall_cards.append(self)
