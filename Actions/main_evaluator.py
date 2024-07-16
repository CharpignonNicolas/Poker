from collections import Counter

class Card:
    suits = ["Coeur", "Carreau", "Trèfle", "Pique"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return f"{self.rank} de {self.suit}"

def evaluate_hand(hand_cards, community_cards):
    all_cards = hand_cards + community_cards
    sorted_cards = sorted(all_cards, key=lambda card: card.rank, reverse=True)

    # Check for flush
    suits = {suit: [] for suit in Card.suits}
    for card in sorted_cards:
        suits[card.suit].append(card)
    
    for suit, cards in suits.items():
        if len(cards) >= 5:
            flush_cards = cards[:5]
            # Check for Royal Flush
            if set(card.rank for card in flush_cards) == {10, 11, 12, 13, 14}:
                return "royal flush", flush_cards
            # Check for Straight Flush
            for i in range(len(flush_cards) - 4):
                if flush_cards[i].rank - flush_cards[i + 4].rank == 4:
                    return "straight flush", flush_cards[i:i + 5]
            return "flush", flush_cards[:5]
    
    # Check for Four of a Kind
    rank_counts = Counter(card.rank for card in sorted_cards)
    four_kind = [rank for rank, count in rank_counts.items() if count == 4]
    if four_kind:
        four_cards = [card for card in sorted_cards if card.rank == four_kind[0]]
        kicker = [card for card in sorted_cards if card.rank != four_kind[0]][0]
        return "four of a kind", four_cards + [kicker]

    # Check for Full House
    three_kind = [rank for rank, count in rank_counts.items() if count == 3]
    pairs = [rank for rank, count in rank_counts.items() if count == 2]
    if three_kind and pairs:
        three_cards = [card for card in sorted_cards if card.rank == three_kind[0]]
        pair_cards = [card for card in sorted_cards if card.rank == pairs[0]]
        return "full house", three_cards[:3] + pair_cards[:2]
    
    # Check for Straight
    ranks = sorted(set(card.rank for card in sorted_cards), reverse=True)
    for i in range(len(ranks) - 4):
        if ranks[i] - ranks[i + 4] == 4:
            straight = [card for card in sorted_cards if card.rank in ranks[i:i + 5]]
            return "straight", straight[:5]
    
    # Check for Three of a Kind
    if three_kind:
        three_cards = [card for card in sorted_cards if card.rank == three_kind[0]]
        kickers = [card for card in sorted_cards if card.rank != three_kind[0]][:2]
        return "three of a kind", three_cards + kickers
    
    # Check for Two Pair
    if len(pairs) >= 2:
        two_pairs = sorted(pairs[:2], reverse=True)
        pair_cards = [card for card in sorted_cards if card.rank in two_pairs]
        kicker = [card for card in sorted_cards if card.rank not in two_pairs][0]
        return "two pair", pair_cards + [kicker]
    
    # Check for One Pair
    if pairs:
        pair_cards = [card for card in sorted_cards if card.rank == pairs[0]]
        kickers = [card for card in sorted_cards if card.rank != pairs[0]][:3]
        return "one pair", pair_cards + kickers

    # High Card
    return "high card", sorted_cards[:5]

def compare_hands(player1, player2, community_cards):
    eval1 = evaluate_hand(player1.hand.cards, community_cards)
    eval2 = evaluate_hand(player2.hand.cards, community_cards)

    hand_ranking = ["high card", "one pair", "two pair", "three of a kind", "straight", "flush", "full house", "four of a kind", "straight flush", "royal flush"]

    if hand_ranking.index(eval1[0]) > hand_ranking.index(eval2[0]):
        return player1
    elif hand_ranking.index(eval1[0]) < hand_ranking.index(eval2[0]):
        return player2
    else:
        for card1, card2 in zip(eval1[1], eval2[1]):
            if card1.rank > card2.rank:
                return player1
            elif card1.rank < card2.rank:
                return player2

        kickers1 = [card.rank for card in player1.hand.cards + community_cards if card not in eval1[1]]
        kickers2 = [card.rank for card in player2.hand.cards + community_cards if card not in eval2[1]]
        for kicker1, kicker2 in zip(sorted(kickers1, reverse=True), sorted(kickers2, reverse=True)):
            if kicker1 > kicker2:
                return player1
            elif kicker1 < kicker2:
                return player2

        return None
