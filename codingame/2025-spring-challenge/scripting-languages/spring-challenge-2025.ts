
type StateAndDepth = string;
type StateRaw = number;
type Score = number;
type TransformationFunction = (stateRaw: StateRaw) => StateRaw;
type State = {
  canonicalState: StateRaw, // canonical representation of the "raw" state
  transform: TransformationFunction // function such that transform(canonicalState) = stateRaw
}

let maxDepth = 1;

const nextStatesCache: Record<StateRaw, State[]> = {};
const scoreCache: Record<StateAndDepth, Score> = {}; // cache the scores for each (state,depth) pair (must keep depth because score is not unique, depends how deep you are)

function getInput(): { initialState: StateRaw, inputMaxDepth: number } {
  // TODO: already implemnted in C++
  return {
    initialState: 0,
    inputMaxDepth: 1,
  }
}

function makeCanonical(sr: StateRaw): State {
  // TODO: almost imlemented already in C++
  // instead of returning a function, we'd return function ID
  return {
    canonicalState: 0,
    transform: (sr: StateRaw) => sr,
  }
}

function calculateNextStatesRaw(sr: StateRaw): StateRaw[] {
  // TODO: implemented already in C++
  return [];
};

function calculateNextStates(s: State): State[] {
  // check cache
  if (nextStatesCache[s.canonicalState] !== undefined) {
    return nextStatesCache[s.canonicalState]
  }

  const nextRawStates: StateRaw[] = calculateNextStatesRaw(s.canonicalState);

  const nextStates: State[] = nextRawStates.map(makeCanonical);
  
  // populate next states cache and return
  nextStatesCache[s.canonicalState] = nextStates;
  return nextStates;
}

function calculateScore(currentState: State, depth: number): Score {
  const { canonicalState, transform } = currentState;

  const stateAndDepth = `${canonicalState}-${depth}`; // can improve with a pair, if pair can be hashed
  if (scoreCache[stateAndDepth] !== undefined) {
    return scoreCache[stateAndDepth];
  }

  if (depth === maxDepth) {
    const currentStateRaw = transform(canonicalState);
    return currentStateRaw as Score;
  }
  
  const nextStates: State[] = calculateNextStates(currentState);

  const nextStatesScores: Score[] = []; // same length as 'nextStates'

  for (const nextState of nextStates) {
    const nextStateScore = calculateScore(nextState, depth + 1);
    const nextStateScoreTransformed = transform(nextStateScore as StateRaw) as Score;
    nextStatesScores.push(nextStateScoreTransformed);
  }

  // populate score cache and return
  const result = nextStatesScores.reduce((acc, score) => acc + score, 0);
  scoreCache[stateAndDepth] = result;
  return result;
}

function main() {
  const { initialState, inputMaxDepth } = getInput();
  
  maxDepth = inputMaxDepth;
  const initialStateCanonical = makeCanonical(initialState);
  const initialStateScoreCanonical = calculateScore(initialStateCanonical, 0); // not sure if starts with 0 or 1

  const initialStateScore = initialStateCanonical.transform(initialStateScoreCanonical as StateRaw) as Score;

  console.log(`Calculated score: ${initialStateScore}`);
}