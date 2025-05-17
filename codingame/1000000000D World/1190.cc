#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main() {
  string a;
  getline(cin, a);
  // cerr << a << endl;
  string b;
  getline(cin, b);
  // cerr << b << endl;

  // Write an answer using cout. DON'T FORGET THE "<< endl"
  // To debug: // cerr << "Debug messages..." << endl;
  istringstream iss_a(a);
  istringstream iss_b(b);

  int64_t dot = 0;
  int64_t n_a, n_b;
  int32_t num_reps_to_squash;
  int32_t rep_a, rep_b;
  iss_a >> rep_a;
  iss_b >> rep_b;
  iss_a >> n_a;
  iss_b >> n_b;
  // cerr << "rep_a: " << rep_a << " n_a: " << n_a << endl;
  // cerr << "rep_b: " << rep_b << " n_b: " << n_b << endl;
  while (rep_a > 0 && rep_b > 0) {
    num_reps_to_squash = min(rep_a, rep_b);
    if (n_a != 0 && n_b != 0) {
      dot += n_a * n_b * num_reps_to_squash;
    }
    // cerr << "dot: " << dot << endl;
    // cerr << "------------------------" << endl;

    rep_a -= num_reps_to_squash;
    if (rep_a <= 0 && !iss_a.eof()) {
      iss_a >> rep_a;
      iss_a >> n_a;
    }
    rep_b -= num_reps_to_squash;
    if (rep_b <= 0 && !iss_b.eof()) {
      iss_b >> rep_b;
      iss_b >> n_b;
    }
  }

  cout << dot << endl;
}