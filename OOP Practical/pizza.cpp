#include<iostream>
#define MAX 5
using namespace std;

class cir_queue
{
    public:
    int front, rear;
    int cq[MAX];
    cir_queue()
    {
        front=-1;
        rear=-1;
    }
    bool isempty()
    {
        return (rear==-1 and front==-1);
    }
    bool isfull()
    {
        return (front==(rear+1)%MAX);
    }
    void enqueue(int ch)
    {
        if(isfull())
        {
            cout<<"CANT TAKE ORDERS! QUEUE IS FULL!!"<<endl;
            return;
        }
        if(isempty())
        {
            rear=0;
            front=0;
        }
        else{
            rear=(rear+1)%MAX;
        }
        cq[rear]=ch;
        cout<<"Order "<<ch<<" Placed successfully!!"<<endl;
    }
    void dequeue()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!"<<endl;
            return;
        }
        cout<<"ORDER NUMBER "<<cq[front]<<" SERVED!!!"<<endl;
        if(rear==front)
        {
            front=-1;
            rear=-1;
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
        cout<<"CURRENT QUEUE: [ ";
        while(1)
        {
            cout<<cq[i]<<" ";
            if(i==rear)
                break;
            i=(i+1)%MAX;
        }
        cout<<"]"<<endl;
    }
};

int main()
{
    cir_queue cq;
    int choice,order;
    do{
        cout << "\nPIZZA PARLOUR Simulation:\n";
        cout << "1. PLACE ORDER\n";
        cout << "2. ORDER SERVED\n";
        cout << "3. DISPLAY ORDER LIST\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch(choice)
        {
            case 1:
            {
                cout<<"ENTER ORDER NUMBER: "<<endl;
                cin>>order;
                cq.enqueue(order);
                break;
            }
            case 2:
            {
                cq.dequeue();
                break;
            }
            case 3:
            {
                cq.display();
                break;
            }
            case 4: {
                cout << "Exiting the program. Goodbye!" << endl;
                break;
            }
            default:
                cout << "INVALID CHOICE. PLEASE TRY AGAIN!" << endl;
                break;
        }
    }while(choice!=4);
    return 0;
}