#include <iostream>
using namespace std;

int main() {
    double x, y;

    cout << "Введите x: ";
    cin >> x;
    cout << "Введите y: ";
    cin >> y;

    bool inArea = (x >= -7) && (x <= 0) &&
                  (y >= -2) && (y <= 0);

    if (inArea)
        cout << "In area" << endl;
    else
        cout << "Out of area" << endl;

    return 0;
}