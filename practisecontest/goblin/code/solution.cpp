#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int caseNum = 0; caseNum < t; caseNum++) {
        int n;
        cin >> n;

        vector<int> boxes(n);
        for (int i = 0; i < n; i++) {
            cin >> boxes[i];
        }

        int m;
        cin >> m;

        long long evenTotal = 0;
        int bigBoxes = 0;

        for (int value : boxes) {
            if (value % 2 == 0) {
                evenTotal += value;
            }
            if (value >= m) {
                bigBoxes++;
            }
        }

        cout << "Even total = " << evenTotal << ", Big boxes = " << bigBoxes;
        if (caseNum < t - 1) {
            cout << endl;
        }
    }

    return 0;
}
