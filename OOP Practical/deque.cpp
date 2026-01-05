#include<iostream>
#define MAX 10
using namespace std;

class deque
{
    public:
    int dq[MAX];
    int rear,front;
    deque()
    {
        rear=-1;
        front=-1;
    }

    bool isfull()
    {
        return ((front==rear+1)||(front==0 && rear==MAX-1));
    }

    bool isempty()
    {
        return (front==-1&&rear==-1);
    }

    void enqueue_front(int x)
    {
        if(isfull())
        {
            cout<<"QUEUE IS FULL!!"<<endl;
            return;
        }
        if(front==0)
        {
            front=MAX-1;
        }
        else if(isempty())
        {
            rear=0;
            front=0;
        }
        else{
            front--;
        }
        dq[front]=x;
    }

    void enqueue_rear(int x)
    {
        if(isfull())
        {
            cout<<"QUEUE IS FULL!!"<<endl;
            return;
        }
        if(isempty())
        {
            rear=0;
            front=0;
        }
        else if(rear==MAX-1)
        {
            rear=0;
        }
        else
        {
            rear++;
        }
        dq[rear]=x;
    }

    void dequeue_front()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!"<<endl;
            return;
        }
        cout<<"DETETING ELEMENT: "<<dq[front]<<endl;
        dq[front] = -1;
        if(front==MAX-1)
        {
            front=0;
        }
        else if (front==rear)
        {
            front=rear=-1;
        }
        else{
            front++;
        }
    }
    void dequeue_rear()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!"<<endl;
            return;
        }
        cout<<"DETETING ELEMENT: "<<dq[rear]<<endl;
        dq[rear] = -1;
        if(rear==0)
        {
            rear=MAX-1;
        }
        else if (front==rear)
        {
            front=rear=-1;
        }
        else{
            rear--;
        }
    }
    void display()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!"<<endl;
            return;
        }
        cout<<"[";
        int i=front;
        cout<<"QUEUE ELEMENTS: [ ";
        while(1)
        {
            if(dq[i]!=-1)
                cout<<dq[i]<<" ";
            if(i==rear)
                break;
            i=(i+1)%MAX;
        }
        cout<<"]"<<endl;
    }
};

int main()
{
    deque d;
    int choice,x;
    do{
        cout << "\nDEQUE :\n";
        cout << "1. INSERT FRONT\n";
        cout << "2. INSERT REAR\n";
        cout << "3. DELETE FRONT\n";
        cout << "4. DELETE REAR\n";
        cout << "5. DISPLAY\n";
        cout << "6. EXIT\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch(choice)
        {
            case 1:
            {
                cout<<"\nENTER VALUE TO ENQUEUE FROM FRONT: "<<endl;
                cin>>x;
                d.enqueue_front(x);
                break;
            }
            case 2:
            {
                cout<<"\nENTER VALUE TO ENQUEUE FROM REAR: "<<endl;
                cin>>x;
                d.enqueue_rear(x);
                break;
            }
            case 3:
            {
                cout<<"\nDELETING ELEMENT FROM FRONT"<<endl;
                d.dequeue_front();
                break;
            }
            case 4:
            {
                cout<<"\nDELETING ELEMENT FROM REAR"<<endl;
                d.dequeue_rear();
                break;
            }
            case 5:
            {
                d.display();
                break;
            }
            case 6: {
                cout << "\nExiting the program. Goodbye!" << endl;
                break;
            }
            default:
                cout << "\nINVALID CHOICE. PLEASE TRY AGAIN!" << endl;
                break;
        }
    }while(choice!=6);
    return 0;
}