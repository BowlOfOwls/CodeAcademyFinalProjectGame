#Define deck and functions
#Created Project 
#Created Github repository
import random
Deck = {}
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

    def deal_me_in(self):
        self.card_drawn=random.choice(list(Deck.keys()))
        print(self.card_drawn)
        Deck[self.card_drawn] -= 1
        if Deck[self.card_drawn] <= 0:
            Deck.pop(self.card_drawn)
        self.cards.append(self.card_drawn)

        self.card_drawn=random.choice(list(Deck.keys()))
        print(self.card_drawn)
        Deck[self.card_drawn] -= 1
        if Deck[self.card_drawn] <= 0:
            Deck.pop(self.card_drawn)
        self.cards.append(self.card_drawn)
    
    def check_cards():
        pass





Brandon = Player("Brandon", "10")
print(Brandon)
Brandon.deal_me_in()
print(Deck)
print(Brandon.cards)