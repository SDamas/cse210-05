import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction_player_1 = Point(constants.CELL_SIZE, 0)
        self._direction_player_2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        player_1_direction = ["a", "d", "w", "s"]
        player_2_direction = ["j", "l", "i", "k"]

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction_player_1 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction_player_1 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction_player_1 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction_player_1 = Point(0, constants.CELL_SIZE)

        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction_player_2 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction_player_2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction_player_2 = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction_player_2 = Point(0, constants.CELL_SIZE)

        snakes = cast.get_actors("snakes")
        player_1 = snakes[0]
        player_2 = snakes[1]

        for key in player_1_direction:
            if self._keyboard_service.is_key_down(key):
                player_1.turn_head(self._direction_player_1)
                player_1.grow_tail(1)

        for key in player_2_direction:
            if self._keyboard_service.is_key_down(key):
                player_2.turn_head(self._direction_player_2)
                player_2.grow_tail(1)
