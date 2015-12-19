# Nicole Ignasiak  
# CIS 125

from BowlingGame import BowlingGame
import unittest

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self._game = BowlingGame()
    
    def rollMany(self, n, pincount):
        for i in range(n):
            self._game.roll(pincount)
    
    # first test    
    def testGutterGame(self):
            self.rollMany(20,0)
            assert self._game.getScore() == 0
            
    # second test
    def testAllOnes(self):
            self.rollMany(20,1)
            assert self._game.getScore() == 20
            
    def testRollSpare(self):
        self._game.roll(5)
        self._game.roll(5)
        self._game.roll(3)
        self.rollMany(17,0)
        assert self._game.getScore() == 16
        
    def testOneStrike(self):
        self.rollStrike()
        self._game.roll(3)
        self._game.roll(4)
        self.rollMany(16,0)
        assert self._game.getScore() == 24
        
    def testPerfectGame(self):
        self.rollMany(12,10)
        assert self._game.getScore() == 300
    
    def rollSpare(self):
        self._game.roll(5)
        self._game.roll(5)
        
    def rollStrike(self):
        self._game.roll(10)