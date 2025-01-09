#include <iostream>
#include <string>

using namespace std;

int main() {
  string input;

  cout << "Enter something: ";
  getline(cin, input);

  cout << "\nPrinting your input 3 times:\n";
  for (int i = 0; i < 3; i++) {
    cout << i + 1 << ": " << input << endl;
  }

  return 0;
}
