from hackathon2.card_game.card import Card
from random import shuffle

class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''

    def __init__(self):
        self.cards = []

    def build(self):
        self.cards = []
        for i in range(len(Card.RANKS)):
            for j in range(len(Card.SUITS)):
                self.cards.append(Card(i, j))
        

    def shuffle_card(self):
        '''Trộn bài'''
        shuffle(self.cards)

    def deal_card(self) -> Card:
        '''Rút một lá bài từ bộ bài'''
        return None if len(self.cards) == 0 else self.cards.pop()
