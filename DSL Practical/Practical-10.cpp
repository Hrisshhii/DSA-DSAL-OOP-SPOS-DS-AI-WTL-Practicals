#include<iostream>
#include<cctype>
using namespace std;
#define size 20 

class stack
{
    public:
    int top;
    char s[size];
    stack()
    {
        top=-1;
    }
    int isempty()
    {
        return(top==-1);
    }
    int isfull()
    {
        return (top==size-1);
    }
    void push(char c)
    {
        if(isfull())
        {
            cout<<"STACK OVERFLOW!!!"<<endl;
            return;
        }
        s[++top]=c;
    }

    char pop()
    {
        if(isempty())
        {
            cout<<"Stack underflow!!!"<<endl;
            return '\0';
        }
        return s[top--];
    }

    char peek()
    {
        if(isempty())
        {
            cout<<"Stack is empty!!"<<endl;
            return '\0';
        }
        else 
            return s[top];
    }
    int precedence(char x)
    {
        if(x=='^')
            return 4;
        else if(x=='*' || x=='/' || x=='%')
            return 3;
        else if(x=='+' || x=='-')
            return 2;
        else
            return 1;
    }

    void conversion(char infix[20],char postfix[20])
    {
        char token;
        int i,j=0;
        for(i=0;infix[i]!='\0';i++)
        {
            token=infix[i];
            if(isalnum(token))
            {
                postfix[j++]=token;
            }
            else if(token=='(')
            {
                push(token);
            }
            else if(token==')')
            {
                while(!isempty() && peek()!='(')
                {
                    postfix[j++]=pop();
                }
                pop();
            }
            else{
                while(!isempty()&&precedence(token)<=precedence(peek()))
                {
                    postfix[j++]=pop();
                }
                push(token);
            }
        }
        while(isempty())
        {
            postfix[j++]=pop();
        }
        postfix[j]='\0';
    }
};

int main()
{
    stack s;
    char postfix[20];
    char infix[20];
    cout<<"ENTER THE INFIX EXPRESSION: "<<endl;
    cin>>infix;
    s.conversion(infix,postfix);
    cout<<"POSTFIX EXPRESSION: "<<postfix;
    return 0;
}