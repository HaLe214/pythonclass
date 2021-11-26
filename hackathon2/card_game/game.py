from typing import List
from hackathon2.card_game.deck import Deck
from hackathon2.card_game.player import Player


class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self.players: List[Player] = []
        self.deck = Deck()
        self.in_game = False

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        if not self.in_game:
            self.deck.shuffle_card()
            self.in_game = True

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        pass

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        print(' -- '.join([player.name for player in self.players]))

    def add_player(self, name):
        '''Thêm một người chơi mới'''
        if len(self.players) > 12:
            print('Du nguoi roi ban oi')
            return
        self.players.append(Player(name))

    def remove_player(self, who: str):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        self.players = [player for player in self.players if player.name != who]

    def deal_card(self):
        '''Chia bài cho người chơi'''
        for player in self.players:
            player.add_card([self.deck.deal_card() for _ in range(3)])

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        for player in self.players:
            print(player.flip_card())
    