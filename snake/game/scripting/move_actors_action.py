from game.scripting.action import Action

class MoveActorsAction(Action):

    def execute(self, cast, script):
        """
        Responsible for moving each actor in the cast.
        """
        actors = cast.get_all_actors()

        for actor in actors:
            actor.move_next()