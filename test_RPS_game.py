import pytest
import RPS_game

test_options = ['Rock', 'Paper', 'Scissors']
test_game_outcomes = [['Rock', 'Rock', 'Nobody'],
                      ['Paper', 'Paper', 'Nobody'],
                      ['Scissors', 'Scissors', 'Nobody'],
                      ['Rock', 'Scissors', 'Player 1'],
                      ['Paper', 'Rock', 'Player 1'],
                      ['Scissors', 'Paper', 'Player 1'],
                      ['Scissors', 'Rock', 'The computer'],
                      ['Paper', 'Scissors', 'The computer'],
                      ['Rock', 'Paper', 'The computer']
                      ]


class TestPlayer:
    def setup_method(self):
        self.player = RPS_game.Player('test')

    def teardown_method(self):
        del self.player

    def test_increase_score(self):
        assert self.player.score == 0
        self.player.increase_score()
        assert self.player.score == 1

    @pytest.mark.parametrize('option', test_options)
    def test_chooses(self, option):
        self.player.chooses(option)
        assert self.player.choice == option

    def test_chooses_invalid(self):
        with pytest.raises(ValueError):
            self.player.chooses('Scissor')

    @pytest.mark.parametrize('execution_number', range(10))
    def test_chooses_random(self, execution_number):
        self.player.chooses_random()
        assert self.player.choice in test_options


class TestGame:
    def setup_method(self):
        self.game = RPS_game.Game()

    def teardown_method(self):
        del self.game

    @pytest.mark.parametrize('user_choice, computer_choice, game_outcome', test_game_outcomes)
    def test_determine_round_winner(self, user_choice, computer_choice, game_outcome):
        self.game.user.chooses(user_choice)
        self.game.computer.chooses(computer_choice)
        self.game.determine_round_winner()
        assert self.game.round_winner == game_outcome

    def test_determine_outcome(self):
        pass

    def test_get_game_info(self):
        pass

    def test_user_selected(self):
        pass




