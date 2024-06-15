class Card:
    # The suits of the cards
    suits = ["Carreau", "Coeur", "Pique", "Trèfle"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 11: Valet, 12: Reine, 13: Roi, 14: As
    rank_names = {11: "Valet", 12: "Reine", 13: "Roi", 14: "As"}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        # Use the rank_names dictionary to get the name if the rank is 11 or higher
        rank = self.rank_names.get(self.rank, str(self.rank))
        return f"{rank} de {self.suit}"