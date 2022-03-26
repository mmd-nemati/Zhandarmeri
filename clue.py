import card

class Clue(card.Card):
    """Repersenation of clues.
    """
    def __init__(self, name):
        self.name = name

def make_clues():
    all_clues = ["man", "rich", "injured", "woman", "jewlery",
                "gov_official", "foot_print", "glasses",
                "vassal", "strong", "red_hair"]
    clues = []
    for i in all_clues:
        str = i
        locals()[str] = Clue(str)
        clues.append(locals()[str])
    return clues 
