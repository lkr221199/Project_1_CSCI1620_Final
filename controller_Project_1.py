from PyQt5.QtWidgets import *
from view_Project_1 import Ui_MainWindow
from RPS_game import Game


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.game = Game()

        self.button_exit.clicked.connect(lambda: self.close())
        self.button_restart.clicked.connect(lambda: self.reset_game())
        self.button_rock.clicked.connect(lambda: self.update_game('Rock'))
        self.button_paper.clicked.connect(lambda: self.update_game('Paper'))
        self.button_scissor.clicked.connect(lambda: self.update_game('Scissor'))

    def update_game(self, user_selection):
        self.game.user_selected(user_selection)
        game_info = self.game.get_game_info()
        self.update_display(game_info)

    def update_display(self, game_info):
        self.lcdNumber_user_score.display(game_info['user_score'])
        self.lcdNumber_computer_score.display(game_info['computer_score'])
        self.label_computer_choice.setText(game_info['computer_choice'])

        if game_info['game_winner'] is None:
            self.label_outcome.setText(f"{game_info['round_winner']} wins this round!\nChoose again")
        else:
            self.label_outcome.setText(f"{game_info['game_winner']} wins the game!\nClick Restart to play again.")
            self.button_scissor.setDisabled(True)
            self.button_paper.setDisabled(True)
            self.button_rock.setDisabled(True)

    def reset_game(self):
        self.game = Game()
        self.label_computer_choice.setText("...")
        self.label_outcome.setText("You are Player 1. Click a button below to play")
        self.lcdNumber_user_score.display("0")
        self.lcdNumber_computer_score.display("0")
        self.button_scissor.setDisabled(False)
        self.button_paper.setDisabled(False)
        self.button_rock.setDisabled(False)

