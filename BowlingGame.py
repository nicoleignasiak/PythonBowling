# Nicole Ignasiak
# CIS 125
# Dr. Neumann

class BowlingGame:
    def __init__(self):
        self._rolls = [0] * 21
        self._current_roll = 0
        
    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll +=1
        
    def getScore(self):
        score = 0
        frameIndex = 0
        for frame in range(10):
            if self.isSpare(frameIndex):
                score += 10 + self._rolls[frameIndex + 2]
                frameIndex += 2
            else:
                score += self._rolls[frameIndex] + self._rolls[frameIndex + 1]
                frameIndex +=2
        return score
        
    def isSpare(self, frameIndex):
        return (self._rolls[frameIndex] + self._rolls[frameIndex+1]) == 10
        
    