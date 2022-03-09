from game.casting.actor import Actor
from game.shared.point import Point
import constants

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, player):
        super().__init__()
        self._points = 0
        self._player = player
        self._position = Point(0,0)

        if self._player == 1:
            self._text = "Player One"
        else: 
            self._text = "Player Two" 
            self._position = constants.PLAYER_2_SCORE 
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"{self._text}: {self._points}")