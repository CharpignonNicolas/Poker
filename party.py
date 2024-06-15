from Players.player import Player
from dealer import Dealer
from pot import Pot
from Rounds.pre_flop import PreFlop
from Rounds.flop import Flop
from Rounds.turn import Turn
from Rounds.river import River
from Actions.betting_round import BettingRound
from Actions.main_evaluator import evaluate_hand, compare_hands

class Party:
    def __init__(self, player_names, initial_stack=1000):
        self.players = [Player(name, initial_stack) for name in player_names]
        self.pot = Pot()
        self.dealer = Dealer()
    
    def start(self):
        # Deal preflop cards and display players' hands
        preflop = PreFlop(self.dealer, self.players)
        print("Preflop")
        self.display_hands()
        self.betting_round()
        self.check_player_status()

        # Add community cards and display after each stage
        flop = Flop(self.dealer)
        print("Flop")
        self.display_community_cards()
        self.betting_round()
        self.check_player_status()

        turn = Turn(self.dealer)
        print("Turn")
        self.display_community_cards()
        self.betting_round()
        self.check_player_status()

        river = River(self.dealer)
        print("River")
        self.display_community_cards()
        self.betting_round()
        self.check_player_status()

        
        # Compare players' hands and display the winner and thhe pot and the cards
        self.evaluate_hands()
        self.compare_hands()
        if player.chips == 0 :
            exit()
        
    
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
        player1, player2 = self.players
        winner = compare_hands(player1, player2, self.dealer.community_cards.cards)
        winner.chips += self.pot.amount
        print(f"{winner.name} wins!")