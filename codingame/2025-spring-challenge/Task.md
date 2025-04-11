# Cephalopods Game State Computation Summary

This problem involves simulating all possible future states of the board game Cephalopods by Mark Steere.

## Game Rules

- Played on a 3x3 grid with dice
- Players take turns adding one die per turn
- New dice must show a 1 unless part of a capturing placement
- For capturing: if a die is placed adjacent to 2+ dice whose values sum to ≤6, those dice must be removed
- The placed die then displays the sum of removed dice values
- If multiple capture combinations exist, the player chooses which to apply
- Captures are mandatory when possible
- Game ends when board is full
- Winner has most dice showing 6 (not needed for this problem)

## The Task

1. Read the initial board state and maximum simulation depth
2. Compute all possible board states after the given number of turns
3. Include games that ended early
4. Calculate a hash for each final board state
5. Sum all hashes modulo 2^30

## Hash Calculation

- Board state represented as a 32-bit integer
- Each square encoded as 0-6 (0 = empty, 1-6 = die value)
- Hash built by iterating squares left-to-right, top-to-bottom
- For each square: shift integer left by 1 digit, add die value

## Expected Output

- The sum of all possible board state hashes modulo 2^30

## Scoring

- Code will be run 10 times per test
- After removing 2 best and 2 worst times, average of remaining 6 runs is the score
- Final score is sum of test scores in milliseconds
- Solution must be optimized for speed

Time limit: 10 seconds for most test cases, with the last two validators having 30 and 40 seconds respectively.
