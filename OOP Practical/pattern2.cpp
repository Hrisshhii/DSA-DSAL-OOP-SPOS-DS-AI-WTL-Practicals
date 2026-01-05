#include <iostream>
#include <math.h>
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
    putpixel(x, y, RED);
    if (dx > dy)
        steps = dx;
    else
        steps = dy;
    xc = dx / steps;
    yc = dy / steps;

    while (i <= steps)
    {
        putpixel(round(x), round(y), RED);
        x = x + xc;
        y = y + yc;
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
    cout<<"ENTER THE CENTER COORDINATES OF THE CIRCLE: "<<endl;
    cin>>xc>>yc;
    cout<<"ENTER THE RADIUS OF THE CIRCLE: "<<endl;
    cin>>r;

    x1=xc;
    y1=yc-r;
    y2=y3=yc+r/2;
    x3=xc-((sqrt(3)/2)*r);
    x2=xc+((sqrt(3)/2)*r);

    bres(xc,yc,r);
    DDA(x1,y1,x2,y2);
    DDA(x3,y3,x2,y2);
    DDA(x3,y3,x1,y1);
    bres(xc,yc,r/2);
    getch();
    closegraph();
    return 0;
}
