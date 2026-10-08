#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double t, x;
    cout << "Введите t: ";
    cin >> t;
    cout << "Введите x: ";
    cin >> x;

    int M = static_cast<int>(t*t*t + 1);
    double y;

    switch (M) {
        case 12:
            y = log(x*x);          // ln(x^2)
            break;

        case 28:
            y = pow(x, 1.2);       // x^1.2
            break;

        case 39:
            y = cos(x*x);          // cos(x^2)
            break;

        case 84:
            y = cos(fabs(x));      // cos(|x|)
            break;

        default:
            cout << "Нет формулы для M = " << M << endl;
            return 0;
    }

    cout << "M = " << M << endl;
    cout << "y = " << y << endl;

    return 0;
}
