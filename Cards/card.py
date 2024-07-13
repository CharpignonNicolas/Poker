import random

# Definition of the Card class
class Card:
    suits = ["carreau", "coeur", "pique", "trefle"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 11: Valet, 12: Reine, 13: Roi, 14: As
    rank_names = {11: "valet", 12: "reine", 13: "roi", 14: "as"}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        rank = self.rank_names.get(self.rank, str(self.rank))
        return f"{rank} de {self.suit}"

    def image_name(self):
        rank = self.rank_names.get(self.rank, str(self.rank))
        return f"{rank}_{self.suit}.png"
