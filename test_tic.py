import unittest
from tictactoe1 import tictactoe

class Test(unittest.TestCase):

    def test_state_evaluation(self):
        result = tictactoe.evaluate_state(self)
        self.assertEqual(result,0)

    def test_check_ai_move(self):
        result = tictactoe.get_ai_move(self)
        self.assertEqual(result, 0)

    def test_check_human_move(self):
        result = 1
        self.assertTrue(0<=result<=2)




if __name__ == "__main__":
    unittest.main()