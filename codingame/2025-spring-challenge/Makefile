# Makefile for sprint-challenge-2025.cc

CXX = clang++
CXXFLAGS = -std=c++17 -Wall -Wextra -pedantic
BENCH = bench.sh
TARGET = spring-challenge-2025
SINGLE_TEST_INPUT = "20 0 5 1 0 0 0 4 0 1" # Result: 738691369
MULTI_TEST_INPUTS = "1 5 5 5 0 0 5 5 5 5" "1 6 1 6 1 0 1 6 1 6" "10 1 1 0 1 0 3 0 1 0" "20 0 5 1 0 0 0 4 0 1" "20 0 6 0 2 2 2 1 6 1" "20 5 0 6 4 5 0 0 6 4" "24 3 0 0 3 6 2 1 0 2" "36 6 0 4 2 0 2 4 0 0" "5 1 1 0 1 0 3 0 1 0" "5 6 6 6 6 6 6 6 0 0" "5 6 6 6 6 6 6 6 6 0" "6 0 6 0 2 2 2 1 6 1" "7 1 1 0 1 0 3 0 1 0" "8 6 0 6 0 0 0 6 1 5" 


all: $(TARGET)

$(TARGET): $(TARGET).cc
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(TARGET).cc

debug: CXXFLAGS += -O0 -g -DDEBUG
debug: clean $(TARGET)

test: CXXFLAGS += -O3
test: clean $(TARGET)
	@for input in $(SINGLE_TEST_INPUT); do \
		echo "Running with test input: $$input"; \
		./$(TARGET) <<< $$input; \
	done

time: CXXFLAGS += -O3
time: clean $(TARGET)
	@for input in $(SINGLE_TEST_INPUT); do \
		echo "Running with test input: $$input"; \
		time ./$(TARGET) <<< $$input; \
	done

bench: CXXFLAGS += -O3
bench: clean $(TARGET)
	@for input in $(MULTI_TEST_INPUTS); do \
		echo "Running benchmark command: time ./$(BENCH) ./$(TARGET) 10 \"$$input\""; \
		time ./$(BENCH) ./$(TARGET) 10 "$$input"; \
	done

clean:
	rm -f $(TARGET)
	
.PHONY: all run debug test clean