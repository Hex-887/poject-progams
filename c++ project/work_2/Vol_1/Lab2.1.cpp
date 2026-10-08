#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x, y;
    cout << "Введите x: ";
    cin >> x;
    cout << "Введите y: ";
    cin >> y;

    bool inArea =
        (x >= 0) &&
        (x <= 5) &&
        (y >= -5) &&
        (y <= 0) &&
        (x*x + y*y >= 16);   // точка вне четверти круга

    if (inArea)
        cout << "Точка принадлежит области" << endl;
    else
        cout << "Точка НЕ принадлежит области" << endl;

    return 0;
}
