class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''

    SUITS = ['♠', '♣', '♦', '♥']
    
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{Card.RANKS[self.rank]} {Card.SUITS[self.suit]}'

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        return (self.rank + 1) * (self.suit + 1) > (other.rank + 1) * (other.suite + 1)
