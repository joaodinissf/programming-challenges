import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

BOOSTABLE_DISTANCE = 1500
MAX_THRUST = 100
POD_RADIUS = 600
RACER_BOI_FACTOR = 1.75
TOO_SLOW_VELOCITY = 7500

BRAKING_DISTANCE = 2 * POD_RADIUS
TOO_CLOSE_DISTANCE_SQUARED = (POD_RADIUS * 1.4) ** 2

have_boost = True
step = 0
last_x = -1
last_y = -1


def dist(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


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

    velocity_x = x - last_x
    velocity_y = y - last_y
    velocity = math.sqrt(velocity_x**2 + velocity_y**2)
    print(f"Velocity: {velocity}", file=sys.stderr, flush=True)
    if velocity < TOO_SLOW_VELOCITY:
        thrust = 100
    else:
        angle_adjustment = max(0, math.cos(math.radians(next_checkpoint_angle)))
        distance_adjustment = min(1, next_checkpoint_dist / BRAKING_DISTANCE)
        thrust = int(MAX_THRUST * angle_adjustment * distance_adjustment)
        thrust = min(MAX_THRUST, int(thrust * RACER_BOI_FACTOR))
        print(f"Setting thrust to {thrust}...", file=sys.stderr, flush=True)

        if (
            have_boost
            and abs(next_checkpoint_angle) < 23
            and (
                dist(x, y, opponent_x, opponent_y) < TOO_CLOSE_DISTANCE_SQUARED
                or next_checkpoint_dist > BOOSTABLE_DISTANCE
            )
        ):
            print("Bye bye--using boost...", file=sys.stderr, flush=True)
            thrust = "BOOST"
            have_boost = False

    target_x = next_checkpoint_x
    target_y = next_checkpoint_y

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(target_x) + " " + str(target_y) + " " + str(thrust))
