import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


my_placements = []
opponent_placements = []


def look_for_potential_ends_at_positions(
    to_play_row, to_play_col, positions, valid_moves, placements
):
    num_pieces = sum([1 for p in positions if p in placements])
    print(
        f"Number of pieces: {num_pieces} for valid moves {valid_moves} and placements {placements}",
        file=sys.stderr,
        flush=True,
    )
    if num_pieces > 1:
        for p in positions:
            if p in valid_moves:
                print(
                    f"Returning position {p} as a potential end for valid moves {valid_moves} and placements {placements}",
                    file=sys.stderr,
                    flush=True,
                )
                return p
    print(
        f"Returning original position {to_play_row, to_play_col}",
        file=sys.stderr,
        flush=True,
    )
    return to_play_row, to_play_col


def look_for_ends(to_play_row, to_play_col, mine, valid_moves, placements):
    if mine:
        row, col = my_placements[-1] if my_placements else (1, 1)
    else:
        row, col = opponent_placements[-1] if opponent_placements else (1, 1)

    # Horizontal
    positions = [(row, i) for i in range(3) if row in range(3) and i in range(3)]
    to_play_row, to_play_col = look_for_potential_ends_at_positions(
        to_play_row, to_play_col, positions, valid_moves, placements
    )

    # Vertical
    if to_play_row == 1 and to_play_col == 1:
        positions = [(i, col) for i in range(3) if i in range(3) and col in range(3)]
        to_play_row, to_play_col = look_for_potential_ends_at_positions(
            to_play_row, to_play_col, positions, valid_moves, placements
        )

    # Diagonal
    if to_play_row == 1 and to_play_col == 1:
        positions = [
            (row + i, col + i)
            for i in range(-2, 3)
            if (row + i) in range(3) and (col + i) in range(3)
        ]
        to_play_row, to_play_col = look_for_potential_ends_at_positions(
            to_play_row, to_play_col, positions, valid_moves, placements
        )

    # Counter-Diagonal
    if to_play_row == 1 and to_play_col == 1:
        positions = [
            (row - i, col + i)
            for i in range(-2, 3)
            if (row - i) in range(3) and (col + i) in range(3)
        ]
        to_play_row, to_play_col = look_for_potential_ends_at_positions(
            to_play_row, to_play_col, positions, valid_moves, placements
        )

    return to_play_row, to_play_col


def look_for_wins(to_play_row, to_play_col, valid_moves):
    return look_for_ends(to_play_row, to_play_col, True, valid_moves, my_placements)


def look_for_threats(to_play_row, to_play_col, valid_moves):
    return look_for_ends(
        to_play_row, to_play_col, False, valid_moves, opponent_placements
    )


# game loop
while True:
    row, col = [int(i) for i in input().split()]
    opponent_placements.append((row, col))

    valid_action_count = int(input())
    valid_moves = [
        (int(i), int(j))
        for i, j in [input().split() for _ in range(valid_action_count)]
    ]

    my_row, my_col = 1, 1
    # Always try to play the center square first
    if (my_row, my_col) not in valid_moves:
        # Look for immediate wins
        print("Looking for wins...", file=sys.stderr, flush=True)
        my_row, my_col = look_for_wins(my_row, my_col, valid_moves)

    if (my_row, my_col) not in valid_moves:
        # Look for immediate threats
        print("Looking for threats...", file=sys.stderr, flush=True)
        my_row, my_col = look_for_threats(my_row, my_col, valid_moves)

    if (my_row, my_col) not in valid_moves:
        # No immediate threats or wins, play first available move instead
        print(
            "No immediate threats or wins, playing first available move...",
            file=sys.stderr,
            flush=True,
        )
        my_row, my_col = valid_moves[0]

    my_placements.append((my_row, my_col))
    print(str(my_row) + " " + str(my_col))
