#include <algorithm>
#include <iostream>
#include <iomanip>
using namespace std;
int main() {
int matrix[3][5] = {
{ 7, 6, 4, 3, 9 },
{ 4, 2, 9, 3, 7 },
{ 8, 3, 4, 6, 2 }
};
for (const auto& row : matrix) {
for (auto x : row) cout << setw(3) << x;
puts("");
}
puts("");
for (auto& row : matrix) sort(begin(row), end(row));
for (const auto& row : matrix) {
for (auto x : row) cout << setw(3) << x;
puts("");
}
system("pause > nul");
}