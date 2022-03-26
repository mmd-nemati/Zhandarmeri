import card
import clues

wall_cards = []

class WallCard(card.Card):
    
    def __init__(self, given_clues):
        self.wall_clues = []
        global wall_cards
        for i in given_clues:
            locals()[i] = clues.Clue(i)
            self.wall_clues.append(locals()[i])
        wall_cards.append(self)

a = WallCard(["woman", "vassal", "red_hair", "strong"])
print(a)