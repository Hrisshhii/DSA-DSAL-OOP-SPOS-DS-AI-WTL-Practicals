#include <iostream>
#include<math.h>
#include<cstdlib>
#include <graphics.h>
using namespace std;

static int LEFT=1,RIGHT=2,BOTTOM=4,TOP=8;
static int xmin,ymin,xmax,ymax;

int getcode(int x,int y)
{
    int code=0;
    if(y>ymax)code |=TOP;
    if(y<ymin)code |=BOTTOM;
    if(x>xmax)code |=RIGHT;
    if(x<xmin)code |=LEFT;
    return code;
}

int main()
{
    int gd=DETECT,gm;
    initgraph(&gd, &gm, NULL);

    cout<<"ENTER THE WINDOW COORDINATES: "<<endl;
    cin>>xmin>>ymin>>xmax>>ymax;

    int x1,y1,x2,y2;
    cout<<"ENTER THE LINE COORDINATES: "<<endl;
    cin>>x1>>y1>>x2>>y2;

    char msg[] = "BEFORE CLIPPING!!";
    outtextxy(200, 50, msg);

    rectangle(xmin,ymin,xmax,ymax);
    line(x1,y1,x2,y2);
    delay(5000);

    int outcode1=getcode(x1,y1);
    int outcode2=getcode(x2,y2);
    int accept=0;

    while(1)
    {
        float m=(float)(y2-y1)/(x2-x1);
        if(outcode1==0 && outcode2==0)
        {
            accept=1;
            break;
        }
        else if((outcode1 & outcode2)!=0)
        {
            break;
        }
        else{
            int x,y;
            int temp;
            if(outcode1!=0)temp=outcode1;
            else temp=outcode2;

            if(temp&TOP){
                x=x1+(ymax-y1)/m;
                y=ymax;
            }
            else if(temp&BOTTOM)
            {
                x=x1+(ymin-y1)/m;
                y=ymin;
            }
            else if(temp&LEFT)
            {
                x=xmin;
                y=y1+(xmin-x1)*m;
            }
            else if (temp&RIGHT)
            {
                x=xmax;
                y=y1+(xmax-x1)*m;
            }

            if(temp==outcode1)
            {
                x1=x;
                y1=y;
                outcode1=getcode(x1,y1);
            }
            else{
                x2=x;
                y2=y;
                outcode2=getcode(x2,y2);
            }
        }
    }

    setcolor(BLUE);
    cleardevice();

    if(accept){
        char msg[] = "AFTER CLIPPING!!";
        outtextxy(200, 50, msg);
        rectangle(xmin,ymin,xmax,ymax);
        line(x1,y1,x2,y2);
    }
    else{
        char msg[] = "AFTER CLIPPING!!";
        outtextxy(200, 50, msg);
        rectangle(xmin,ymin,xmax,ymax);
    }
    getch();
    closegraph();
    return 0;

}