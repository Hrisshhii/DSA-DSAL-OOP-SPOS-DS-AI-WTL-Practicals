#include<iostream>
using namespace std;
#define size 5

class deque
{
    public:
    int front,rear,q[size],n;
    deque()
    {
        front=-1;
        rear=-1;
        n=size;
    }
    int isempty()
    {
        return (rear==-1&&front==-1);
    }
    int isfull()
    {
        return ((front==0 && rear==size-1)||(front==rear+1));
    }
    void enqueue_front(int x)
    {
        if(isfull())
        {
            cout<<"QUEUE IS FULL!!!"<<endl;
            return;
        }
        else if (front==-1&&rear==-1)
        {
            front=0;
            rear=0;
        }
        else if (front==0)
        {
            front=size-1;
        }
        else
        {
            front--;
        }
        q[front]=x;
    }
    void enqueue_rear(int x)
    {
        if(isfull())
        {
            cout<<"QUEUE IS FULL!!!!"<<endl;
            return;
        }
        else if(isempty())
        {
            front=rear=0;
        }
        else if(rear==size-1)
        {
            rear=0;
        }
        else{
            rear++;
        }
        q[rear]=x;
    }
    void dequeue_rear()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!!";
            return;
        }
        cout<<"ELEMENT DELETED: "<<q[rear]<<endl;
        if(rear==0)
        {
            rear=size-1;
        }
        else if(rear==front)
        {
            rear=-1;
            front=-1;
        }
        else{
            rear--;
        }
    }
    void dequeue_front(){
        if(isempty())
        {
            cout<<"Queue is empty!!!"<<endl;
            return;
        }
        cout<<"ELEMENT DELETED: "<<q[front]<<endl;
        if(front==rear)
        {
            front=rear=-1;
        }
        else if(front==size-1)
        {
            front=0;
        }
        else{
            front++;
        }
    }
    void display()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!!"<<endl;
            return;
        }
        int i=front;
        while(true)
        {
            cout<<q[i]<<" ";
            if(i==rear)
                break;
            i=(i+1)%size;
        }
        cout<<endl;
    }
};

int main()
{
    deque dq;
    dq.enqueue_front(10);
    dq.enqueue_front(20);
    dq.enqueue_rear(30);
    dq.enqueue_rear(40);
    dq.display();

    dq.dequeue_front();
    dq.display();

    dq.dequeue_rear();
    dq.display();

    dq.enqueue_rear(50);
    dq.enqueue_front(100);
    dq.enqueue_front(60);
    dq.enqueue_front(110);
    dq.display();
    return 0;
}