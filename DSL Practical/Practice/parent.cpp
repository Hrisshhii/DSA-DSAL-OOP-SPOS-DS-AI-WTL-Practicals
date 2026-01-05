#include<iostream>
using namespace std;
#define MAX 10

class stack
{
    public:
    int top;
    char s[MAX];
    stack()
    {
        top=-1;
    }
    bool isempty()
    {
        return (top==-1);
    }
    bool isfull()
    {
        return (top==MAX-1);
    }

    void push(char x)
    {
        if(isfull())
        {
            cout<<"STACK IS FULL!!"<<endl;
            return;
        }
        top++;
        s[top]=x;
    }

    void pop()
    {
        if(isempty())
        {
            cout<<"STACK IS EMPTY!!"<<endl;
            return;
        }
        top--;
    }

    char peek()
    {
        if(isempty())
        {
            cout<<"STACK IS EMPTY!!"<<endl;
            return 0;
        }
        return s[top];
    }

    void checkparenthesis()
    {
        int flag=1;
        string eq;
        cout<<"ENTER THE EQUATION TO CHECK PARENTESIS: "<<endl;
        cin>>eq;
        for(int i=0;eq[i]!='\0';i++)
        {
            if(eq[i]=='(' || eq[i]=='[' || eq[i]=='{')
                push(eq[i]);
            else if(((eq[top]=='('&&eq[i]==')') || (eq[top]=='['&&eq[i]==']') || (eq[top]=='{'&&eq[i]=='}'))&&!isempty())
                pop();
            else
            {
                flag=0;
                break;
            }
        }
        if(flag==1 && isempty())
            cout<<"WELL PARENTHESIZED!!"<<endl;
        else
            cout<<"NOT WELL PARENTHESIZED!!"<<endl;
    }
};

int main()
{
    stack s;
    s.checkparenthesis();
    return 0;
}