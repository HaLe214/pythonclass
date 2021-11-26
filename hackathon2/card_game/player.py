from typing import List
from hackathon2.card_game.card import Card
from functools import reduce


class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self, name: str):  # dễ
        self.name = name
        self.cards: List[Card] = []

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        return reduce(lambda a, b: a + b, [card.rank for card in self.cards])

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        return max(self.cards)

    def add_card(self, cards: List[Card]):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self.cards = cards

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.cards = []

    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        return '-'.join([str(card) for card in self.cards])
