import random


class Player:
    def __init__(self, name):
        self.choices = ('Rock', 'Paper', 'Scissor')
        self.name = name
        self.score = 0
        self.choice = None

    def increase_score(self):
        self.score += 1

    def chooses(self, choice):
        if choice in self.choices:
            self.choice = choice
        else:
            raise ValueError(f'{choice} not one of {self.choices}')

    # random choice generator
    def chooses_random(self):
        self.chooses(self.choices[random.randint(0, 2)])


class Game:
    def __init__(self, num_rounds=3):
        self.num_rounds = num_rounds
        self.user = Player('Player 1')
        self.computer = Player('The computer')
        self.round_winner = None
        self.game_winner = None

    def user_selected(self, selection):
        self.user.chooses(selection)
        self.computer.chooses_random()
        self.__determine_round_winner()
        self.__determine_outcome()

    def __determine_round_winner(self):
        if self.user.choice == self.computer.choice:
            self.round_winner = 'Nobody'
        if self.user.choice == 'Rock' and self.computer.choice == 'Scissor':
            self.round_winner = self.user.name
        elif self.user.choice == 'Paper' and self.computer.choice == 'Rock':
            self.round_winner = self.user.name
        elif self.user.choice == 'Scissor' and self.computer.choice == 'Paper':
            self.round_winner = self.user.name
        elif self.user.choice == 'Scissor' and self.computer.choice == 'Rock':
            self.round_winner = self.computer.name
        elif self.user.choice == 'Rock' and self.computer.choice == 'Paper':
            self.round_winner = self.computer.name
        elif self.user.choice == 'Paper' and self.computer.choice == 'Scissor':
            self.round_winner = self.computer.name

        # call increase_score() on the winner
        if self.round_winner == self.computer.name:
            self.computer.increase_score()
        elif self.round_winner == self.user.name:
            self.user.increase_score()

    def __determine_outcome(self):
        if self.user.score > self.num_rounds / 2:
            self.game_winner = self.user.name

        elif self.computer.score > self.num_rounds / 2:
            self.game_winner = self.computer.name

    def get_game_info(self):
        return {'user_choice': self.user.choice,
                'user_score': self.user.score,
                'computer_choice': self.computer.choice,
                'computer_score': self.computer.score,
                'round_winner': self.round_winner,
                'game_winner': self.game_winner}
