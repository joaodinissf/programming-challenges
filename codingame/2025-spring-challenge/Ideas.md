# From Claude

  1. Bit-packing for board representation: Instead of a 9-digit number, use bit representation (could fit in 32 bits: 3-4 bits per position) to reduce memory usage and speed up operations.
  2. Replace position_as_vector with direct access: The extraction of digits is expensive; consider a different board representation or inline the position_as_vector creation where needed.
  3. Pre-computed lookup tables: Create lookup tables for common operations based on board patterns to avoid repeated calculations.
  4. Remove the calculate_next_captures function: It's not used except for validation. Remove it and the assert_functional_equivalence_v2 function to simplify the code.
  5. Pool allocator for vectors: Implement a custom allocator for next_positions to reduce memory allocation overhead.
  6. Partial memoization: Instead of caching entire next positions, cache intermediate calculation results.
  7. SIMD optimization: Use vector instructions (AVX/SSE) for parallel operations on board positions.
  8. Compile-time generation: Move some of the constant arrays to compile-time computations using constexpr.
  9. Optimize data structures: Consider using flat_hash_map from abseil or robin_hood hash for potentially faster lookups than unordered_map.

# Priority

  Try bit packing
  Add another preprocessor directive to control whether to use v1 or v2
  Then run the benchmark with each of these options

# Handy

738691369

20 0 5 1 0 0 0 4 0 1
1 5 5 5 0 0 5 5 5 5
1 6 1 6 1 0 1 6 1 6
