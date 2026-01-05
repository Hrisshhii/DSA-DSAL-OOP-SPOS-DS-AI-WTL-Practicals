#include<iostream>
using namespace std;
#define size 10

class queue
{
    public:
    int q[size];
    int front,rear;
    queue()
    {
        front=-1;
        rear=-1;
    }
    int isempty()
    {
        return (front==-1&&rear==-1);
    }
    int isfull()
    {
        return (rear==size-1);
    }
    void enqueue(int x)
    {
        if(isfull())
        {
            cout<<"QUEUE IS FULL!!!"<<endl;
            return;
        }
        else if(isempty())
        {
            rear=0;
            front=0;
            q[rear]=x;
        }
        else 
        {
            rear++;
            q[rear]=x;
        }
    }
    void dequeue()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!!"<<endl;
            return;
        }
        else if(rear==front)
        {
            rear=-1;
            front=-1;
        }
        else
        {
            front++;
        }
    }
    void display()
    {
        if (isempty())
        {
            cout << "QUEUE IS EMPTY!!!" << endl;
            return;
        }
        int i;
        for(i=front;i<=rear;i++)
        {
            cout<<q[i]<<" ";
        }
        cout<<endl;
    }
};
int main()
{
    queue qu;
    qu.enqueue(10);
    qu.enqueue(20);
    qu.enqueue(30);
    qu.enqueue(40);
    qu.display();
    qu.dequeue();
    qu.dequeue();
    qu.display();
    return 0;
}