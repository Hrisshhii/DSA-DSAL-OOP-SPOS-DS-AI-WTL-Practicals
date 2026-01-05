#include<iostream>
using namespace std;
#define MAX 5

class PizzaParlor
{
    public:
    int front,rear,queue[MAX];
    PizzaParlor()
    {
        front=rear=-1;
    }
    bool isfull()
    {
        return (front==(rear+1)%MAX);
    }
    bool isempty()
    {
        return (front==-1);
    }
    void enqueue(int order)
    {
        if(isfull())
        {
            cout<<"QUEUE IS FULL!! CANT TAKE ORDERS!!!"<<endl;
            return;
        }
        if(isempty())
        {
            front=rear=0;
        }
        else
            rear=(rear+1)%MAX;
        queue[rear]=order;
        cout<<"ORDER "<<order<<" placed successfully!!!"<<endl;
    }
    void dequeue()
    {
        if(isempty())
        {
            cout<<"QUEUE EMPTY!!! NO ORDERS TO DELETE!!!"<<endl;
            return;
        }
        cout<<"ORDER COMPLETED: "<<queue[front]<<endl;
        if(front==rear)
        {
            front=rear=-1;
        }
        else
            front=(front+1)%MAX;
    }
    void display()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!"<<endl;
            return;
        }
        int i=front;
        while(true)
        {
            cout<<queue[i]<<" ";
            if(i==rear)
                break;
            i=(i+1)%MAX;
        }
        cout<<endl;
    }
};

int main()
{
    PizzaParlor p;
    p.enqueue(10);
    p.enqueue(20);
    p.enqueue(30);
    p.enqueue(40);
    p.display();
    p.dequeue();
    p.dequeue();
    p.display();
    p.enqueue(45);
    p.enqueue(50);
    p.display();
    p.enqueue(60);
    p.enqueue(70);
    p.enqueue(80);
    p.display();
    p.dequeue();
    p.dequeue();
    p.dequeue();
    p.dequeue();
    p.display();
    return 0;
}