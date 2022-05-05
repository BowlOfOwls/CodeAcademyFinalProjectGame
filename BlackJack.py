#Define deck and functions
#Created Project 
#Created Github repository
from pdb import post_mortem
import random
Deck = {}
pot = 0
def shuffle_deck():
    for i in range(1,11):
        if i == 10:
            Deck[i] = 16
        else:    
            Deck[i] = 4
        
# print(Deck)
class Player:
    def __init__(self, input_name, input_money):
        self.name = input_name
        self.money = input_money
        self.greetings =random.choice(["Howdy", "Greetings", "Good meetings"])
        self.refer =random.choice(["friend", "friendo", "buddy", "chum"])
        self.currency = random.choice(["bucks", "dollars", "moolah"])
        self.cards = []
        self.card_drawn =0

    def __repr__(self):
        description = "{greeting}, {greetingrefer} my name is {name} and it is my pleasure to deal you in. I still got {money} {currency} to spare.".format(greeting= self.greetings, greetingrefer= self.refer, name = self.name, money=self.money, currency = self.currency)
        return description

    def hit_me(self):
        self.card_drawn=random.choice(list(Deck.keys()))
        print(self.card_drawn)
        Deck[self.card_drawn] -= 1
        if Deck[self.card_drawn] <= 0:
            Deck.pop(self.card_drawn)
        self.cards.append(self.card_drawn)
        print("Total value is now {value}".format(value = sum(self.cards)))

    def deal_me_in(self, wager, pot):
        self.hit_me()
        self.hit_me()
        self.money -= wager
        pot = pot + wager
    
    def compare(self, player_2, pot):
        my_score = sum(self.cards)
        player_2_score = sum(player_2.cards)
        if my_score > player_2_score:
            player_2.money += pot 
        elif player_2_score > my_score:
            self.money += pot 
        shuffle_deck()
        self.cards = []
        player_2.cards = []
    
    def check_cards():
        pass




shuffle_deck()
Brandon = Player("Brandon", 10)
print(Brandon)
Brandon.deal_me_in(5, pot)
print(Brandon.cards)
Matthew = Player("Brandon", 10)
print(Matthew)
Matthew.deal_me_in(5, pot)
print(Brandon.cards)

Matthew.compare(Brandon, pot)
print(Matthew.money)