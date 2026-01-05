#include <iostream>
#include <math.h>
#include <graphics.h>
#define MAX 10
using namespace std;

int main() 
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);
    int a[3][MAX];
    int choice, n;

    cout << "ENTER THE NUMBER OF VERTEX IN SEQUENCE: " << endl;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "ENTER COORDINATES (x, y): " << endl;
        cin >> a[0][i] >> a[1][i];
        a[2][i] = 1;
    }

    setcolor(RED);
    for (int i = 0; i < n - 1; i++) {
        line(a[0][i], a[1][i], a[0][i + 1], a[1][i + 1]);
    }
    line(a[0][n - 1], a[1][n - 1], a[0][0], a[1][0]);

    do {
        cout << "\n\n\nMENU\n\n\n1. Translate\n2. Scaling\n3. Rotation\n4. EXIT" << endl;
        cout << "ENTER YOUR CHOICE: " << endl;
        cin >> choice;

        switch (choice) {
        case 1: { // Translation
            int tx, ty, result[3][MAX];
            cout << "ENTER THE TRANSLATION VALUES (tx, ty): " << endl;
            cin >> tx >> ty;
            int m[3][3] = {
                {1, 0, tx},
                {0, 1, ty},
                {0, 0, 1}
            };

            for (int i = 0; i < n; i++) {
                result[0][i] = m[0][0] * a[0][i] + m[0][1] * a[1][i] + m[0][2] * a[2][i];
                result[1][i] = m[1][0] * a[0][i] + m[1][1] * a[1][i] + m[1][2] * a[2][i];
                result[2][i] = 1;
            }

            setcolor(BLUE);
            for (int i = 0; i < n - 1; i++) {
                line(result[0][i], result[1][i], result[0][i + 1], result[1][i + 1]);
            }
            line(result[0][n - 1], result[1][n - 1], result[0][0], result[1][0]);
            break;
        }

        case 2: { // Scaling
            float sx, sy;
            int result[3][MAX];
            cout << "ENTER THE SCALING FACTORS (sx, sy): " << endl;
            cin >> sx >> sy;

            float m[3][3] = {
                {sx, 0, 0},
                {0, sy, 0},
                {0, 0, 1}
            };

            for (int i = 0; i < n; i++) {
                result[0][i] = m[0][0] * a[0][i] + m[0][1] * a[1][i] + m[0][2] * a[2][i];
                result[1][i] = m[1][0] * a[0][i] + m[1][1] * a[1][i] + m[1][2] * a[2][i];
                result[2][i] = 1;
            }

            setcolor(GREEN);
            for (int i = 0; i < n - 1; i++) {
                line(result[0][i], result[1][i], result[0][i + 1], result[1][i + 1]);
            }
            line(result[0][n - 1], result[1][n - 1], result[0][0], result[1][0]);
            break;
        }

        case 3: { // Rotation
            float angle;
            int result[3][MAX];
            cout << "ENTER THE ROTATION ANGLE (in degrees): " << endl;
            cin >> angle;

            float rad = angle * M_PI / 180.0;

            float m[3][3] = {
                {cos(rad), -sin(rad), 0},
                {sin(rad), cos(rad), 0},
                {0, 0, 1}
            };

            for (int i = 0; i < n; i++) {
                result[0][i] = m[0][0] * a[0][i] + m[0][1] * a[1][i] + m[0][2] * a[2][i];
                result[1][i] = m[1][0] * a[0][i] + m[1][1] * a[1][i] + m[1][2] * a[2][i];
                result[2][i] = 1;
            }

            setcolor(YELLOW);
            for (int i = 0; i < n - 1; i++) {
                line(result[0][i], result[1][i], result[0][i + 1], result[1][i + 1]);
            }
            line(result[0][n - 1], result[1][n - 1], result[0][0], result[1][0]);
            break;
        }

        case 4:
            cout << "EXITING... :)" << endl;
            break;

        default:
            cout << "INCORRECT ENTRY!!!" << endl;
            break;
        }
    } while (choice != 4);

    getch();
    closegraph();
    return 0;
}
