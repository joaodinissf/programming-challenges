import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

POD_RADIUS = 600
START_SLOWING_DISTANCE = 1200
FAR_AWAY_DISTANCE = 5000
TOO_CLOSE_DISTANCE_SQUARED = 160000
have_boost = True
step = 0


def dist(x1, y1, x2, y2):
    return (x2 - x1) ^ 2 + (y2 - y1) ^ 2


# game loop
while True:
    step += 1
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    (
        x,
        y,
        next_checkpoint_x,
        next_checkpoint_y,
        next_checkpoint_dist,
        next_checkpoint_angle,
    ) = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 0
    else:
        thrust = 100

    # if next_checkpoint_dist > POD_RADIUS and next_checkpoint_dist < START_SLOWING_DISTANCE:
    #     thrust = int(thrust * (1 - (next_checkpoint_dist - POD_RADIUS) / (START_SLOWING_DISTANCE - POD_RADIUS)))

    if (
        have_boost
        and step > 100
        and next_checkpoint_dist >= FAR_AWAY_DISTANCE
        and abs(next_checkpoint_angle) < 23
    ):
        print("Using boost...", file=sys.stderr, flush=True)
        thrust = "BOOST"
        have_boost = False

    # if  < next_checkpoint_dist:
    #     target_x = opponent_x
    #     target_y = opponent_y
    # else:
    target_x = next_checkpoint_x
    target_y = next_checkpoint_y

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(target_x) + " " + str(target_y) + " " + str(thrust))
