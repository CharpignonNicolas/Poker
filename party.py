from Players.player import Player
from dealer import Dealer
from pot import Pot
from Rounds.pre_flop import PreFlop
from Rounds.flop import Flop
from Rounds.turn import Turn
from Rounds.river import River
from Actions.betting_round import BettingRound
from Actions.main_evaluator import evaluate_hand, compare_hands
from Cards.card import Card

class Party:
    def __init__(self, player_names, initial_stack=1000):
        self.players = [Player(name, initial_stack) for name in player_names]
        self.pot = Pot()
        self.dealer = Dealer()
        self.stage = "preflop"
    
    def start(self):
        preflop = PreFlop(self.dealer, self.players)
        print("Preflop")
        self.display_hands()
    
    def next_stage(self):
        if self.stage == "preflop":
            self.betting_round()
            self.check_player_status()
            self.stage = "flop"
            flop = Flop(self.dealer)
            print("Flop")
        elif self.stage == "flop":
            self.display_community_cards()
            self.betting_round()
            self.check_player_status()
            self.stage = "turn"
            turn = Turn(self.dealer)
            print("Turn")
        elif self.stage == "turn":
            self.display_community_cards()
            self.betting_round()
            self.check_player_status()
            self.stage = "river"
            river = River(self.dealer)
            print("River")
        elif self.stage == "river":
            self.display_community_cards()
            self.betting_round()
            self.check_player_status()
            self.stage = "showdown"
        elif self.stage == "showdown":
            self.evaluate_hands()
            self.compare_hands()
            self.stage = "end"
    
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
