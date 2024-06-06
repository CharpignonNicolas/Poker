from player import Player
from dealer import Dealer
from pot import Pot
from pre_flop import PreFlop
from flop import Flop
from turn import Turn
from river import River
from betting_round import BettingRound
from main_evaluator import evaluate_hand, compare_hands

# Function to check the status of players
def check_player_status():
    if player1.in_game == False and player2.in_game == False:
        print("Both players folded. Game over.")
        exit()
    elif player1.in_game == False:
        print("Player 1 folded. Player 2 wins!")
        exit()
    elif player2.in_game == False:
        print("Player 2 folded. Player 1 wins!")
        exit()

# Create players, the pot, and the dealer
player1 = Player("Player 1", 1000)
player2 = Player("Player 2", 1000)
pot = Pot()
dealer = Dealer()

# Deal preflop cards and display players' hands
preflop = PreFlop(dealer, [player1, player2])
print(player1)
print(player2)
betting_round1 = BettingRound([player1, player2])
betting_round1.round()
check_player_status()
print(pot)

# Add community cards and display after each stage
flop = Flop(dealer)
print(dealer.community_cards)
betting_round2 = BettingRound([player1, player2])
betting_round2.round()
check_player_status()
print(pot)

turn = Turn(dealer)
print(dealer.community_cards)
betting_round3 = BettingRound([player1, player2])
betting_round3.round()
check_player_status()
print(pot)

river = River(dealer)
print(dealer.community_cards)
betting_round4 = BettingRound([player1, player2])
betting_round4.round()
check_player_status()
print(pot)

# Evaluate players' hands and display
eval1 = evaluate_hand(player1.hand.cards, dealer.community_cards.cards)
print(f"Player 1's hand: {eval1[1]} ({eval1[0]})")
eval2 = evaluate_hand(player2.hand.cards, dealer.community_cards.cards)
print(f"Player 2's hand: {eval2[1]} ({eval2[0]})")

# Compare players' hands and display the winner
winner = compare_hands(player1, player2, dealer.community_cards)
if winner == player1:
    print("Player 1 wins!")
elif winner == player2:
    print("Player 2 wins!")
else:
    print("It's a tie!")
