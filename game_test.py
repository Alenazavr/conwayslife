import unittest
import game

class TestGame(unittest.TestCase):

    def testInput(self):
        conway = game.conways_life()
        conway.data[0][0]=1
        conwayTwo = game.conways_life()
        self.assertNotEqual(conway.getData(), conwayTwo.getData())

    def testNewGen(self):
        conway = game.conways_life()
        # если у клетки есть три живых соседа то она становится живой
        # * * *
        #   *   - эта оживает
        conway.data[0][0]=1
        conway.data[1][0]=1
        conway.data[2][0]=1
        conway.next_generation()
        self.assertEqual(conway.data[1][1], 1)

    def testNewGen2(self):
        conway = game.conways_life()
        conway.data[0][0] = 1
        conway.data[1][0] = 1
        conway.data[2][0] = 1
        conway.next_generation()
        conway.next_generation()
        self.assertEqual(conway.data[1][1], 0)

    def testNewGen3(self):
        conway = game.conways_life()
        conway.data[0][3] = 1
        conway.data[1][2] = 1
        conway.data[2][1] = 1
        conway.next_generation()
        self.assertEqual(conway.data[2][1], 0)
        self.assertEqual(conway.data[0][3], 0)
        self.assertEqual(conway.data[1][2], 1)

    def testNewGen4(self):
        conway = game.conways_life()
        conway.data[0][1] = 1
        conway.next_generation()
        self.assertEqual(conway.data[0][1], 0)

if __name__ == '__main__':
    unittest.main()