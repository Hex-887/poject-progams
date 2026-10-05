#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a, b;

    cout << "Введите a: ";
    cin >> a;
    cout << "Введите b: ";
    cin >> b;

    double y = sqrt(pow(a - b, 2)) / pow(b, 2);

    cout << "y = " << y << endl;

    return 0;
}