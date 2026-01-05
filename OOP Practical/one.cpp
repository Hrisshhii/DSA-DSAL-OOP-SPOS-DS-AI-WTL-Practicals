#include <iostream>
#include <cmath>
#include <graphics.h>
using namespace std;

void DDA(int x1, int y1, int x2, int y2)
{
    float dx, dy, x, y, steps, xc, yc;
    int i = 1;
    dx = abs(x2 - x1);
    dy = abs(y2 - y1);
    x = x1;
    y = y1;
    
    // Use integer rounding for pixel placement
    putpixel(round(x), round(y), RED);

    // Determine steps based on the line's direction (steep or flat)
    if (dx > dy)
        steps = dx;
    else
        steps = dy;

    // Calculate increments
    xc = dx / steps;
    yc = dy / steps;

    // Draw the line
    while (i <= steps)
    {
        x = x + xc;
        y = y + yc;
        putpixel(round(x), round(y), RED); // Round to nearest integer for correct pixel placement
        i++;
        delay(2);
    }
}

void bres(int xc, int yc, int r)
{
    int p, x, y;
    x = 0;
    y = r;

    p = 3 - (r * 2);
    do
    {
        putpixel(xc + x, yc + y, 1);
        putpixel(xc - x, yc - y, 2);
        putpixel(xc + x, yc - y, 3);
        putpixel(xc - x, yc + y, 4);
        putpixel(xc + y, yc + x, 5);
        putpixel(xc + y, yc - x, 6);
        putpixel(xc - y, yc + x, 7);
        putpixel(xc - y, yc - x, 5);
        if (p < 0)
            p = p + (4 * x) + 6;
        else
        {
            p = p + ((x - y) * 4 + 10);
            y = y - 1;
        }
        x = x + 1;
        delay(25);
    } while (x < y);
}

int main()
{
    int gd = DETECT, gm;
    int x1, y1, x2, y2, x3, y3, r, xc, yc;
    initgraph(&gd, &gm, NULL);

    // Input for circle center and radius
    cout << "ENTER THE CENTER COORDINATES OF THE CIRCLE: " << endl;
    cin >> xc >> yc;
    cout << "ENTER THE RADIUS OF THE CIRCLE: " << endl;
    cin >> r;

    // Calculate triangle vertices based on the circle's center and radius
    x1 = xc;
    y1 = yc - r;
    y2 = y3 = yc + r / 2;
    x3 = xc - ((sqrt(3) / 2) * r);
    x2 = xc + ((sqrt(3) / 2) * r);

    // Debugging: Print the coordinates
    cout << "Triangle Vertex 1: (" << x1 << ", " << y1 << ")" << endl;
    cout << "Triangle Vertex 2: (" << x2 << ", " << y2 << ")" << endl;
    cout << "Triangle Vertex 3: (" << x3 << ", " << y3 << ")" << endl;

    // Draw circle and triangle
    bres(xc, yc, r);  // Draw the circle
    DDA(x1, y1, x2, y2);  // Line 1
    DDA(x3, y3, x2, y2);  // Line 2
    DDA(x3, y3, x1, y1);  // Line 3 (this is the problematic line)

    // Draw smaller circle
    bres(xc, yc, r / 2);  // Smaller circle

    getch();
    closegraph();
    return 0;
}
