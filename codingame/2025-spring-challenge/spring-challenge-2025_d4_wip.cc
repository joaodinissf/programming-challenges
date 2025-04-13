#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

// TODO Consider reverting some of these to uint8_t, but I was getting trouble
using GameStateInt = uint32_t;
using GameStateArray = array<uint32_t, 9>;
using CanonicalGameState = GameStateInt;
using TransformationCounts = array<uint32_t, 8>;
using TransformationId = uint32_t;
using GameStateAsCanonical = pair<GameStateInt, uint32_t>;

// This lookup table defines the result of applying transformation id2 after
// transformation id1
const TransformationId FUSED_TRANSFORMATIONS[8][8] = {
    {0, 1, 2, 3, 4, 5, 6, 7}, // id1 = 0 (identity)
    {1, 2, 3, 0, 7, 4, 5, 6}, // id1 = 1 (rotate 90)
    {2, 3, 0, 1, 6, 7, 4, 5}, // id1 = 2 (rotate 180)
    {3, 0, 1, 2, 5, 6, 7, 4}, // id1 = 3 (rotate 270)
    {4, 5, 6, 7, 0, 1, 2, 3}, // id1 = 4 (horizontal reflection)
    {5, 6, 7, 4, 3, 0, 1, 2}, // id1 = 5 (diagonal reflection)
    {6, 7, 4, 5, 2, 3, 0, 1}, // id1 = 6 (vertical reflection)
    {7, 4, 5, 6, 1, 2, 3, 0}  // id1 = 7 (counter-diagonal reflection)
};

const TransformationId INVERSE_TRANSFORMATIONS[8] = {
    0, // Identity
    3, // 90° rotation
    2, // 180° rotation
    1, // 270° rotation
    4, // Horizontal reflection
    5, // Diagonal reflection
    6, // Vertical reflection
    7  // Counter-diagonal reflection
};

// The first number in each vector is the index of the square where the move is
// made The second to last numbers in each vector are the potential neighbors to
// be captured
const vector<vector<vector<int32_t>>> CAPTURING_POSSIBILITIES = {
    {{1, 3}}, //

    {{0, 2, 4}, {0, 2}, {0, 4}, {2, 4}}, //

    {{1, 5}}, //

    {{0, 4, 6}, {0, 4}, {0, 6}, {4, 6}}, //

    {{1, 3, 5, 7},
     {1, 3, 5},
     {1, 3, 7},
     {1, 5, 7},
     {3, 5, 7},
     {1, 3},
     {1, 5},
     {1, 7},
     {3, 5},
     {3, 7},
     {5, 7}}, //

    {{2, 4, 8}, {2, 4}, {2, 8}, {4, 8}}, //

    {{3, 7}}, //

    {{4, 6, 8}, {4, 6}, {4, 8}, {6, 8}}, //

    {{5, 7}}, //
};

unordered_map<CanonicalGameState,
              unordered_map<CanonicalGameState, TransformationCounts>>
    next_positions_cache;

void pretty_print_game_state(const GameStateArray &arr) {
  for (int i = 0; i < 9; i++) {
    cerr << static_cast<int>(arr[i]);
    if (i % 3 == 2)
      cerr << endl;
  }
  cerr << endl;
}

GameStateArray inline game_state_int_to_array(const GameStateInt &matrix) {
  // Input: 012345678
  // Output: [0,1,2,3,4,5,6,7,8]

  GameStateArray arr{}; // Initialize with default values
  GameStateInt temp_matrix = matrix;
  for (int32_t i = 8; i >= 0; i--) {
    arr[i] = temp_matrix % 10;
    temp_matrix /= 10;
  }
  return arr;
}

GameStateInt inline game_state_array_to_int(const GameStateArray &matrix) {
  // Input: [0,1,2,3,4,5,6,7,8]
  // Output: 012345678

  GameStateInt result = 0;
  for (int32_t i = 0; i < 9; i++) {
    result = result * 10 + matrix[i];
  }
  return result;
}

GameStateArray rotate_matrix_90_clockwise(const GameStateArray &matrix) {
  // Input: [0,1,2,3,4,5,6,7,8] represents:
  // 0 1 2
  // 3 4 5
  // 6 7 8

  // Output: [6,3,0,7,4,1,8,5,2] represents:
  // 6 3 0
  // 7 4 1
  // 8 5 2

  return {matrix[6], matrix[3], matrix[0], matrix[7], matrix[4],
          matrix[1], matrix[8], matrix[5], matrix[2]};
}

GameStateArray rotate_matrix_180(const GameStateArray &matrix) {
  // Input: [0,1,2,3,4,5,6,7,8] represents:
  // 0 1 2
  // 3 4 5
  // 6 7 8

  // Output: [8,7,6,5,4,3,2,1,0] represents:
  // 8 7 6
  // 5 4 3
  // 2 1 0

  return {matrix[8], matrix[7], matrix[6], matrix[5], matrix[4],
          matrix[3], matrix[2], matrix[1], matrix[0]};
}

GameStateArray rotate_matrix_270_clockwise(const GameStateArray &matrix) {
  // Input: [0,1,2,3,4,5,6,7,8] represents:
  // 0 1 2
  // 3 4 5
  // 6 7 8

  // Output: [2,5,8,1,4,7,0,3,6] represents:
  // 2 5 8
  // 1 4 7
  // 0 3 6

  return {matrix[2], matrix[5], matrix[8], matrix[1], matrix[4],
          matrix[7], matrix[0], matrix[3], matrix[6]};
}

GameStateArray reflect_matrix_horizontal(const GameStateArray &matrix) {
  // Input: [0,1,2,3,4,5,6,7,8] represents:
  // 0 1 2
  // 3 4 5
  // 6 7 8

  // Output: [6,7,8,3,4,5,0,1,2] represents:
  // 6 7 8
  // 3 4 5
  // 0 1 2

  return {matrix[6], matrix[7], matrix[8], matrix[3], matrix[4],
          matrix[5], matrix[0], matrix[1], matrix[2]};
}

GameStateArray reflect_matrix_diagonal(const GameStateArray &matrix) {
  // Input: [0,1,2,3,4,5,6,7,8] represents:
  // 0 1 2
  // 3 4 5
  // 6 7 8

  // Output: [0,3,6,1,4,7,2,5,8] represents:
  // 0 3 6
  // 1 4 7
  // 2 5 8

  return {matrix[0], matrix[3], matrix[6], matrix[1], matrix[4],
          matrix[7], matrix[2], matrix[5], matrix[8]};
}

GameStateArray reflect_matrix_vertical(const GameStateArray &matrix) {
  // Input: [0,1,2,3,4,5,6,7,8] represents:
  // 0 1 2
  // 3 4 5
  // 6 7 8

  // Output: [2,1,0,5,4,3,8,7,6] represents:
  // 2 1 0
  // 5 4 3
  // 8 7 6

  return {matrix[2], matrix[1], matrix[0], matrix[5], matrix[4],
          matrix[3], matrix[8], matrix[7], matrix[6]};
}

GameStateArray reflect_matrix_counterdiagonal(const GameStateArray &matrix) {
  // Input: [0,1,2,3,4,5,6,7,8] represents:
  // 0 1 2
  // 3 4 5
  // 6 7 8

  // Output: [8,5,2,7,4,1,6,3,0] represents:
  // 8 5 2
  // 7 4 1
  // 6 3 0

  return {matrix[8], matrix[5], matrix[2], matrix[7], matrix[4],
          matrix[1], matrix[6], matrix[3], matrix[0]};
}

GameStateArray get_nth_transformation(const GameStateArray &matrix,
                                      const TransformationId &id) {
  // Apply the transformation with the given id to the matrix
  switch (id) {
  case 0:
    return matrix; // Identity
  case 1:
    return rotate_matrix_90_clockwise(matrix); // 90° rotation
  case 2:
    return rotate_matrix_180(matrix); // 180° rotation
  case 3:
    return rotate_matrix_270_clockwise(matrix); // 270° rotation
  case 4:
    return reflect_matrix_horizontal(matrix); // Horizontal reflection
  case 5:
    return reflect_matrix_diagonal(matrix); // Diagonal reflection
  case 6:
    return reflect_matrix_vertical(matrix); // Vertical reflection
  case 7:
    return reflect_matrix_counterdiagonal(
        matrix); // Counter-diagonal reflection
  default:
    assert(false && "Invalid transformation id");
    return {};
  }
}

TransformationId fuse_transformations(const TransformationId &id1,
                                      const TransformationId &id2) {
  return FUSED_TRANSFORMATIONS[id1][id2];
}

GameStateAsCanonical get_matrix_canonical_form(const GameStateArray &matrix) {
  // Apply all 8 possible transformations and find the one with lowest
  // lexicographical rank

  array<GameStateArray, 8> all_forms = {
      matrix,                                // Identity
      rotate_matrix_90_clockwise(matrix),    // 90° rotation
      rotate_matrix_180(matrix),             // 180° rotation
      rotate_matrix_270_clockwise(matrix),   // 270° rotation
      reflect_matrix_horizontal(matrix),     // Horizontal reflection
      reflect_matrix_diagonal(matrix),       // Diagonal reflection
      reflect_matrix_vertical(matrix),       // Vertical reflection
      reflect_matrix_counterdiagonal(matrix) // Counter-diagonal reflection
  };

  // Calculate the base-10 representation of each matrix form for easy
  // comparison
  array<GameStateInt, 8> form_values;
  for (size_t i = 0; i < 8; i++) {
    form_values[i] = game_state_array_to_int(all_forms[i]);
  }

  // Find the index of the minimum value
  auto min_it = min_element(form_values.begin(), form_values.end());
  TransformationId transformation_id =
      INVERSE_TRANSFORMATIONS[distance(form_values.begin(), min_it)];
  CanonicalGameState canonical_state = *min_it;

  return make_pair(canonical_state, transformation_id);
}

GameStateAsCanonical get_matrix_canonical_form(const GameStateInt &matrix) {
  GameStateArray arr = game_state_int_to_array(matrix);
  return get_matrix_canonical_form(arr);
}

void add_to_next_positions_cache(
    const GameStateArray &capture_state,
    unordered_map<CanonicalGameState, TransformationCounts> &next_positions) {
  // Convert to canonical form and add to next positions
  auto canonical_form = get_matrix_canonical_form(capture_state);

  auto it = next_positions.find(canonical_form.first);
  if (it != next_positions.end()) {
    // Key already exists, increment the count
    it->second[canonical_form.second]++;
  } else {
    // Key does not exist, initialize the counts
    TransformationCounts transformation_counts{};
    transformation_counts.fill(0); // Initialize all counts to 0
    transformation_counts[canonical_form.second] = 1;
    next_positions[canonical_form.first] = transformation_counts;
  }
}

void memoize_next_positions(const GameStateInt &game_state,
                            const GameStateArray &game_state_array) {
  unordered_map<CanonicalGameState, TransformationCounts> next_positions = {};

  // For each empty position on the board, check all possible moves
  for (int pos = 0; pos < 9; pos++) {
    if (game_state_array[pos] != 0) { // Non-empty position, skip
      continue;
    }

    bool have_captured = false;

    // Check all capturing possibilities for this position
    for (const auto &capturing_option : CAPTURING_POSSIBILITIES[pos]) {
      // Check if this capturing option is valid (all neighbors must have dice)
      bool valid_capture = true;
      int capture_sum = 0;

      // Start from index 1 since index 0 is the position itself
      for (size_t i = 0; i < capturing_option.size(); i++) {
        int neighbor_pos = capturing_option[i];
        if (game_state_array[neighbor_pos] == 0) {
          valid_capture = false;
          break;
        }
        capture_sum += game_state_array[neighbor_pos];
      }

      // If valid capture and sum <= 6, create the capture move
      if (valid_capture && capture_sum > 0 && capture_sum <= 6) {
        have_captured = true;

        // Create a new state with this capture
        GameStateArray capture_state = game_state_array;
        capture_state[pos] = capture_sum; // Place die with capture sum value

        // Remove captured dice
        for (size_t i = 0; i < capturing_option.size(); i++) {
          int neighbor_pos = capturing_option[i];
          capture_state[neighbor_pos] = 0;
        }

        add_to_next_positions_cache(capture_state, next_positions);
      }
    }

    // If no captures were possible, add the simple die placement
    if (!have_captured) {
      // Create a new state with a die placed at this position
      GameStateArray next_state = game_state_array;
      next_state[pos] = 1; // Place die with value 1

      add_to_next_positions_cache(next_state, next_positions);
    }
  }

  next_positions_cache[game_state] = next_positions;
}

// Calculate contribution to result with modulo 2^30 to prevent overflow
void add_state_to_result(const GameStateArray &canonical_array,
                         const TransformationId &transform_id,
                         const int32_t count, int32_t &result) {
  // Get the actual game state by applying the inverse transformation
  GameStateArray actual_array =
      get_nth_transformation(canonical_array, transform_id);
  GameStateInt actual_state = game_state_array_to_int(actual_array);

  // Add to result, using modulo 2^30 to prevent overflow
  // Apply modulo at each step to prevent overflow
  int32_t mod = (1 << 30);
  int64_t intermediate = (int64_t)(actual_state % mod) * (count % mod);
  result = (result + intermediate % mod) % mod;
}

void final_step(unordered_map<GameStateInt, TransformationCounts> &game_states,
                int32_t &result) {
  for (const auto &[canonical_state, transformation_counts] : game_states) {
    GameStateArray canonical_array = game_state_int_to_array(canonical_state);
    for (TransformationId transform_id = 0; transform_id < 8; transform_id++) {
      if (transformation_counts[transform_id] > 0) {
        add_state_to_result(canonical_array, transform_id,
                            transformation_counts[transform_id], result);
      }
    }
  }
}

void intermediate_step(
    unordered_map<GameStateInt, TransformationCounts> &game_states,
    int32_t &result) {
  unordered_map<GameStateInt, TransformationCounts> next_game_states;

  for (const auto &state : game_states) {
    GameStateInt current_state = state.first;
    GameStateArray current_state_arr = game_state_int_to_array(current_state);
    const TransformationCounts &transformation_counts = state.second;

    if (next_positions_cache.find(current_state) ==
        next_positions_cache.end()) {
      memoize_next_positions(current_state, current_state_arr);
    }

    // Get the memoized next positions for the canonical state
    auto &next_states = next_positions_cache[current_state];
    if (next_states.empty()) {
      for (size_t transformation_id = 0;
           transformation_id < transformation_counts.size();
           transformation_id++) {
        const auto &transformation_count =
            transformation_counts[transformation_id];
        if (transformation_count == 0) {
          continue;
        }

        // Calculate contribution to result
        add_state_to_result(current_state_arr, transformation_id,
                            transformation_count, result);
      }
      continue;
    }

    for (const auto &next_state : next_states) {
      // TODO There is a bug here, it could be that the state has already been
      // added to next_game_states, but with a different transformation
      // counts. We need to merge the transformation counts instead of
      // overwriting them.

      next_game_states.insert(next_state); // Insert the next state

      TransformationCounts next_transformation_counts = {};
      next_transformation_counts.fill(0);

      for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
          if (transformation_counts[i] > 0 && next_state.second[j] > 0) {
            // Fuse the transformations
            TransformationId fused_transformation_id =
                fuse_transformations(j, i);
            next_transformation_counts[fused_transformation_id] +=
                transformation_counts[i] * next_state.second[j];
          }
        }
      }

      next_game_states[next_state.first] = next_transformation_counts;
    }
  }

  // Debug output - print next_game_states
  cerr << "Next game states:" << endl;
  for (const auto &[state, counts] : next_game_states) {
    cerr << "State: " << state << " Counts: [";
    for (size_t i = 0; i < counts.size(); ++i) {
      cerr << static_cast<int32_t>(counts[i]);
      if (i < counts.size() - 1)
        cerr << ", ";
    }
    cerr << "]" << endl;
  }

  game_states = next_game_states;
}

void hash_all_leaf_nodes(
    unordered_map<GameStateInt, TransformationCounts> &game_states,
    int32_t &result, const int32_t &current_depth, const int32_t &max_depth) {
  if (current_depth == max_depth) {
    final_step(game_states, result);
  } else {
    intermediate_step(game_states, result);
  }
}

void get_input(int32_t &max_depth, int32_t &board) {
  cin >> max_depth;
  cin.ignore();

  int32_t digit = 100000000;
  for (int32_t i = 0; i < 3; i++) {
    for (int32_t j = 0; j < 3; j++) {
      int32_t value;
      cin >> value;
      cin.ignore();

      board += value * digit;
      digit /= 10;
    }
  }
}

int32_t main() {
  // TODO Revisit
  // next_positions_cache.reserve(1 << 18); // needed for the longer inputs

  int32_t max_depth;
  int32_t board = 0;
  get_input(max_depth, board);

  // cerr << "Max depth: " << max_depth << endl;
  // cerr << "Initial board: " << board << endl;

  // Initialize the map with the starting position
  unordered_map<GameStateInt, TransformationCounts> next_game_states;
  GameStateAsCanonical game_state_canonical = get_matrix_canonical_form(board);
  next_game_states[game_state_canonical.first] =
      {}; // Empty transformation counts for the initial state
  next_game_states[game_state_canonical.first][game_state_canonical.second] = 1;

  int32_t result = 0;
  int32_t current_depth = 0;

  // Process all positions at each depth level
  while (!next_game_states.empty()) {
    // cerr << "depth: " << current_depth << "/" << max_depth << "\r" <<
    // flush;
    hash_all_leaf_nodes(next_game_states, result, current_depth, max_depth);
    current_depth++;
  }

  cerr << endl;
  cerr << "Final hash: " << result << endl;

  cout << result << endl;
}
