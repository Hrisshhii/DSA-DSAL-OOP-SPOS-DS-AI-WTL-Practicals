#include <iostream>
#include <math.h>
#include <graphics.h>
using namespace std;

void koch(int x1,int y1,int x2,int y2,int it)
{
    float angle=(60*3.14)/180;
    int x3=(2*x1+x2)/3;
    int y3=(2*y1+y2)/3;
    int x4=(x1+x2*2)/3;
    int y4=(y1+y2*2)/3;

    int x=x3+(x4-x3)*cos(angle)+(y4-y3)*sin(angle);
    int y=y3-(x4-x3)*sin(angle)+(y4-y3)*cos(angle);

    if(it>0)
    {
        koch(x1,y1,x3,y3,it-1);
        koch(x3,y3,x,y,it-1);
        koch(x,y,x4,y4,it-1);
        koch(x4,y4,x2,y2,it-1);
    }
    else{
        line(x1,y1,x3,y3);
        line(x3,y3,x,y);
        line(x,y,x4,y4);
        line(x4,y4,x2,y2);
    }
    delay(10);
}

int main()
{
    int gd = DETECT, gm;
    int x1, y1, x2, y2, order;
    initgraph(&gd, &gm, NULL);
    cout<<"ENTER THE COORDINATE X1: "<<endl;
    cin>>x1;
    cout<<"ENTER THE COORDINATE Y1: "<<endl;
    cin>>y1;
    cout<<"ENTER THE COORDINATE X2: "<<endl;
    cin>>x2;
    cout<<"ENTER THE COORDINATE Y2: "<<endl;
    cin>>y2;
    cout<<"ORDER OF THE KOCH: "<<endl;
    cin>>order;
    koch(x1,y1,x2,y2,order);
    getch();
    closegraph();
    return 0;
}