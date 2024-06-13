from Cards.card import Card

# Function to evaluate a player's hand
def evaluate_hand(hand_cards, community_cards):
    # Combine the player's hand cards and the community cards
    all_cards = hand_cards + community_cards

    # Sort the cards by rank
    sorted_cards = sorted(all_cards, key=lambda card: card.rank, reverse=True)

    # Check for a royal flush
    flush_cards = [card for card in sorted_cards if card.suit == sorted_cards[0].suit]
    if len(flush_cards) >= 5:
        flush_cards = flush_cards[:5]
        if flush_cards[-1].rank == 14:
            return "royal flush", flush_cards

    # Check for a straight flush
    if len(flush_cards) >= 5:
        return "straight flush", flush_cards[:5]

    # Check for four of a kind
    for i in range(len(sorted_cards) - 3):
        if sorted_cards[i].rank == sorted_cards[i + 3].rank:
            return "four of a kind", sorted_cards[i:i + 4]

    # Check for a full house
    for i in range(len(sorted_cards) - 2):
        if sorted_cards[i].rank == sorted_cards[i + 2].rank:
            for j in range(len(sorted_cards) - 1):
                if j != i and sorted_cards[j].rank == sorted_cards[j + 1].rank:
                    return "full house", sorted_cards[i:i + 3] + sorted_cards[j:j + 2]

    # Check for a flush
    suits = {suit: [] for suit in Card.suits}
    for card in sorted_cards:
        suits[card.suit].append(card)
    for suit, cards in suits.items():
        if len(cards) >= 5:
            return "flush", cards[:5]

    # Check for a straight
    ranks = [card.rank for card in sorted_cards]
    ranks = list(sorted(set(ranks), reverse=True))
    for i in range(len(ranks) - 4):
        if ranks[i] - ranks[i + 4] == 4:
            straight = [card for card in sorted_cards if card.rank in ranks[i:i + 5]]
            return "straight", straight

    # Check for three of a kind
    for i in range(len(sorted_cards) - 2):
        if sorted_cards[i].rank == sorted_cards[i + 2].rank:
            return "three of a kind", sorted_cards[i:i + 3]

    # Check for two pair
    pairs = []
    for i in range(len(sorted_cards) - 1):
        if sorted_cards[i].rank == sorted_cards[i + 1].rank:
            pairs.append(sorted_cards[i])
            pairs.append(sorted_cards[i + 1])
    if len(pairs) >= 4:
        return "two pair", pairs[:4]

    # Check for one pair
    pairs = []
    for i in range(len(sorted_cards) - 1):
        if sorted_cards[i].rank == sorted_cards[i + 1].rank:
            pairs.append(sorted_cards[i])
            pairs.append(sorted_cards[i + 1])
    if len(pairs) >= 2:
        return "one pair", pairs[:2] + sorted_cards[:3]

    # High card
    return "high card", sorted_cards[:5]

def compare_hands(player1, player2, community_cards):
    eval1 = evaluate_hand(player1.hand.cards, community_cards)
    eval2 = evaluate_hand(player2.hand.cards, community_cards)

    if eval1[0] > eval2[0]:
        return player1
    elif eval1[0] < eval2[0]:
        return player2
    else:
        # If the hands have the same rank, compare the cards that compose them
        for card1, card2 in zip(eval1[1], eval2[1]):
            if card1.rank > card2.rank:
                return player1
            elif card1.rank < card2.rank:
                return player2

        # If the cards are identical, compare the kickers
        kickers1 = [card.rank for card in player1.hand.cards + community_cards if card not in eval1[1]]
        kickers2 = [card.rank for card in player2.hand.cards + community_cards if card not in eval2[1]]
        for kicker1, kicker2 in zip(sorted(kickers1, reverse=True), sorted(kickers2, reverse=True)):
            if kicker1 > kicker2:
                return player1
            elif kicker1 < kicker2:
                return player2

        # If the kickers are also identical, it's a tie
        return None
