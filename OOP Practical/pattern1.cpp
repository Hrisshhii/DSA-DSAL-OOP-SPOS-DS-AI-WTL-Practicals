#include <iostream>
#include<math.h>
#include <graphics.h>
using namespace std;

void DDA(int x1,int y1,int x2,int y2)
{
    float dx,dy,x,y,steps,xc,yc;
    int i=1;
    dx=abs(x2-x1);
    dy=abs(y2-y1);
    x=x1;
    y=y1;
    putpixel(x,y,RED);
    if(dx>dy)
        steps=dx;
    else steps=dy;
    xc=dx/steps;
    yc=dy/steps;

    while(i<=steps)
    {
        putpixel(x,y,RED);
        x=x+xc;
        y=y+yc;
        i++;
        delay(2);
    }
}

void bres(int xc,int yc,int r)
{
    int p,x,y;
    x=0;
    y=r;

    p=3-(r*2);
    do
    {
        putpixel(xc+x,yc+y,1);
        putpixel(xc-x,yc-y,2);
        putpixel(xc+x,yc-y,3);
        putpixel(xc-x,yc+y,4);
        putpixel(xc+y,yc+x,5);
        putpixel(xc+y,yc-x,6);
        putpixel(xc-y,yc+x,7);
        putpixel(xc-y,yc-x,5);
        if(p<0)
            p=p+(4*x)+6;
        else
        {
            p=p=((x-y)*4+10);
            y=y-1;
        }
        x=x+1;
        delay(25);
    } while (x<y);
}

int main()
{
    int gd=DETECT,gm;
    int x1,y1,x2,y2,x3,y3,x4,y4,r,xc,yc;
    int x5,y5,x6,y6,x7,y7,x8,y8;
    initgraph(&gd,&gm,NULL);
    cout<<"ENTER X1: "<<endl;
    cin>>x1;
    cout<<"ENTER Y1: "<<endl;
    cin>>y1;
    cout<<"ENTER X3: "<<endl;
    cin>>x3;
    cout<<"ENTER Y3: "<<endl;
    cin>>y3;

    x4=x1;
    y4=y3;
    x2=x3;
    y2=y1;

    x5=(x1+x2)/2;
    y5=y1;
    x7=(x4+x3)/2;
    y7=y3;
    y6=(y3+y2)/2;
    x6=x2;
    y8=(y1+y4)/2;
    x8=x1;

    int d,D;
    d=x2-x1;
    D=y4-y1;

    r=(d*D)/(2*sqrt((D*D)+(d*d)));
    xc=x5;
    yc=y8;

    DDA(x1,y1,x2,y2);
    DDA(x2,y2,x3,y3);
    DDA(x4,y4,x3,y3);
    DDA(x1,y1,x4,y4);

    DDA(x5,y5,x6,y6);
    DDA(x6,y6,x7,y7);
    DDA(x7,y7,x8,y8);
    DDA(x8,y8,x5,y5);

    bres(xc,yc,r);
    getch();
    closegraph();
    return 0;
}