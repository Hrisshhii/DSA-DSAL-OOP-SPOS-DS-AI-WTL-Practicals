#include<iostream>
using namespace std;
#define size 10
class stack{
    public:
    char s[size];
    int top;
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

    void pop()
    {
        if(isempty())
        {
            cout<<"Stack underflow!!!"<<endl;
            return;
        }
        top--;
    }

    void peek()
    {
        if(isempty())
        {
            cout<<"Stack underflow!!!"<<endl;
        }
        else
        {
            cout<<"TOP ELEMENT IS "<<s[top]<<endl;
        }
    }

    void check_paranthesis()
    {
        int flag=1;
        string eq;
        cout<<"ENTER THE DATA TO CHECK PARENTESIS: "<<endl;
        cin>>eq;
        for(int l=0;eq[l]!='\0';l++){
            if(eq[l]=='(' || eq[l]=='[' || eq[l]=='{'){
                push(eq[l]);
            }
            else if((eq[top]=='('&&!isempty()&& eq[l]==')') || (eq[top]=='['&&!isempty()&& eq[l]==']') || (eq[top]=='{'&&!isempty()&& eq[l]=='}'))
            {
                pop();
            }
            else
            {
                flag=0;
                break;
            }
        }
        if (isempty()&&flag==1)
            cout<<"WELL PARANTHESIZED!!!"<<endl;
        else
            cout<<"NOT PARANTHESIZED!!!"<<endl;
    }
};
int main()
{
    stack st;
    st.check_paranthesis();
    return 0;
}
