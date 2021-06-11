import random
from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        paddle = cast["paddle"][0]  # there's only one
        ball = cast["ball"][0]  # there's only one
        bricks = cast["brick"]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)
                velocity = ball.get_velocity()
                velocity = velocity.reverse_y()
                ball.set_velocity(velocity)
                break

        # Bounce ball on paddle
        if ball.get_position().get_x() >= paddle.get_position().get_x() and ball.get_position().get_x() <= paddle.get_position().get_x() + 10 and ball.get_position().get_y() == paddle.get_position().get_y():
            velocity = ball.get_velocity()
            velocity = velocity.reverse_y()
            ball.set_velocity(velocity)

        # Quit game is ball tocuh floor
        elif ball.get_position().get_y() >= 21:
            quit()

        # Bounce ball on wall
        if ball.get_position().get_x() == 1 or ball.get_position().get_x() == 79:
            velocity = ball.get_velocity()
            velocity = velocity.reverse_x()
            ball.set_velocity(velocity)

        # Bounce ball on wall
        if ball.get_position().get_y() == 1:
            velocity = ball.get_velocity()
            velocity = velocity.reverse_y()
            ball.set_velocity(velocity)
