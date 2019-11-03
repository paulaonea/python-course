from unittest import TestCase
from rock_paper_scissors import result


class Test(TestCase):
    def test_wins(self):
        win_options = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]
        for i, j in win_options:
            self.assertEqual(result(i, j), 'won')

    def test_loses(self):
        lose_options = [('scissors', 'rock'), ('rock', 'paper'), ('paper', 'scissors')]
        for i, j in lose_options:
            self.assertEqual(result(i, j), 'lost')

    def test_draws(self):
        draw_options = [('rock', 'rock'), ('paper', 'paper'), ('scissors', 'scissors')]
        for i, j in draw_options:
            self.assertEqual(result(i, j), 'draw')
