import unittest
from inference.tt_entails import tt_entails


class TestTtEntails(unittest.TestCase):

    def test_tt_entails(self):
        knowledge_base = list()
        sentence = 'a sentence'
        result = tt_entails(knowledge_base, sentence)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()