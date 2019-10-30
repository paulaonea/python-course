from unittest import TestCase
from rock_paper_scissors import result


class Test(TestCase):
    def test_1(self):
        self.assertEqual(result('rock', 'paper'), "lost")

    def test_2(self):
        self.assertEqual(result('paper', 'rock'), "won")

    def test_3(self):
        self.assertEqual(result('rock', 'scissors'), "won")

    def test_4(self):
        self.assertEqual(result('scissors', 'rock'), "lost")

    def test_5(self):
        self.assertEqual(result('scissors', 'paper'), "won")

    def test_6(self):
        self.assertEqual(result('paper', 'scissors'), "lost")

    def test_7(self):
        draw_options = [('rock', 'rock'), ('paper', 'paper'), ('scissors', 'scissors')]
        for i, j in draw_options:
            self.assertEqual(result(i, j), 'draw')
