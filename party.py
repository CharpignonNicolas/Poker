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
import pygame

class Party:
    def __init__(self, player_names, screen, font, buttons, inputBox, initial_stack=1000):
        self.players = [Player(name, initial_stack) for name in player_names]
        self.pot = Pot()
        self.screen = screen
        self.font = font
        self.buttons = buttons
        self.inputBox = inputBox
        self.dealer = Dealer()
        self.stage = "preflop"
        self.betting_round = BettingRound(self.players, self.pot, self.screen, self.font, self.buttons, self.inputBox)
        print(f"Screen: {self.screen}, Font: {self.font}")  # Debugging line

    def start(self):
        preflop = PreFlop(self.dealer, self.players)
        print("Preflop")
        self.display_hands()
        self.betting_round.round()

        flop = Flop(self.dealer)    
        print("Flop")
        self.display_community_cards()
        self.display_hands()
        self.betting_round.round()  

    def handle_event(self, event):
        self.betting_round.handle_buttons_event(event)

    def display_hands(self):
        for player in self.players:
            print(player)
        print(self.pot)

        
    def display_community_cards(self):
        print(self.dealer.community_cards)

    def reset_players_status(self):
        for player in self.players:
            player.status = None
