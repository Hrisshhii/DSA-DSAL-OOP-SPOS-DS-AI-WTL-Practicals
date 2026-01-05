#include<iostream>
#define MAX 10
using namespace std;

class jobqueue
{
    public:
    int rear,front;
    string job[MAX];
    jobqueue()
    {
        rear=-1;
        front=-1;
    }
    bool isfull()
    {
        return (rear==MAX-1);
    }
    bool isempty()
    {
        return (front==-1);
    }
    void push(string s)
    {
        if(isfull())
        {
            cout<<"THE QUEUE IS FULL"<<endl;
            return;
        }
        if(isempty())
        {
            front=0;
        }
            rear++;
            job[rear]=s;
            cout<<"JOB "<<s<<" ADDED TO JOB QUEUE!!"<<endl;
    }

    void pop()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!"<<endl;
            return;
        }
        cout<<"DELETING JOB "<<job[front]<<endl;
        front++;
    }

    void display()
    {
        if(isempty())
        {
            cout<<"QUEUE IS EMPTY!!"<<endl;
            return;
        }
        cout << "Current jobs in the queue: ";
        for(int i=front;i<=rear;i++)
        {
            cout << job[i] << " ";
        }
        cout<<endl;
    }
};

int main()
{
    jobqueue jq;
    string job;
    int choice;
    do{
        cout << "\nJob Queue Simulation:\n";
        cout << "1. Add Job\n";
        cout << "2. Delete Job\n";
        cout << "3. Display Queue\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch(choice)
        {
            case 1:
            {
                cout<<"Enter job name to add: "<<endl;
                cin.ignore();
                getline(cin,job);
                jq.push(job);
                break;
            }
            case 2:
            {
                jq.pop();
                break;
            }
            case 3:
            {
                jq.display();
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