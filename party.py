from player import Player
from dealer import Dealer
from pot import Pot
from pre_flop import PreFlop
from flop import Flop
from turn import Turn
from river import River
from betting_round import BettingRound
from main_evaluator import evaluate_hand, compare_hands

class Party:
    def __init__(self, player_names, initial_stack=1000):
        self.players = [Player(name, initial_stack) for name in player_names]
        self.pot = Pot()
        self.dealer = Dealer()
    
    def start(self):
        # Deal preflop cards and display players' hands
        preflop = PreFlop(self.dealer, self.players)
        self.display_hands()
        self.betting_round()
        self.check_player_status()

        # Add community cards and display after each stage
        flop = Flop(self.dealer)
        self.display_community_cards()
        self.betting_round()
        self.check_player_status()

        turn = Turn(self.dealer)
        self.display_community_cards()
        self.betting_round()
        self.check_player_status()

        river = River(self.dealer)
        self.display_community_cards()
        self.betting_round()
        self.check_player_status()

        # Evaluate players' hands and display
        self.evaluate_hands()
        # Compare players' hands and display the winner
        self.compare_hands()
    
    def display_hands(self):
        for player in self.players:
            print(player)
        print(self.pot)

    def display_community_cards(self):
        print(self.dealer.community_cards)
    
    def betting_round(self):
        betting_round = BettingRound(self.players, self.pot)
        betting_round.round()

    def check_player_status(self):
        active_players = [player for player in self.players if player.in_game]
        if len(active_players) == 0:
            print("All players folded. Game over.")
            exit()
        elif len(active_players) == 1:
            print(f"{active_players[0].name} wins!")
            exit()

    def evaluate_hands(self):
        for player in self.players:
            eval_hand = evaluate_hand(player.hand.cards, self.dealer.community_cards.cards)
            print(f"{player.name}'s hand: {eval_hand[1]} ({eval_hand[0]})")

    def compare_hands(self):
        best_player = None
        best_hand = None

        for player in self.players:
            if player.in_game:
                current_hand = evaluate_hand(player.hand.cards, self.dealer.community_cards.cards)
                if not best_hand or compare_hands(current_hand, best_hand) > 0:
                    best_hand = current_hand
                    best_player = player

        if best_player:
            print(f"{best_player.name} wins!")
        else:
            print("It's a tie!")
