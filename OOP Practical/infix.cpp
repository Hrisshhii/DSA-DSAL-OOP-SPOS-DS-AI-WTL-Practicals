#include<iostream>
#define MAX 100
using namespace std;

class stack
{
    public:
    char st[MAX];
    int top;
    stack()
    {
        top=-1;
    }
    bool isempty(){
        return (top==-1);
    }
    bool isfull(){
        return (top==MAX-1);
    }
    void push(int ch){
        if(isfull())
        {
            cout<<"STACK IS FULL!!"<<endl;
            return;
        }
        top++;
        st[top]=ch;
    }
    char pop(){
        if(isempty())
        {
            cout<<"STACK IS EMPTY!!"<<endl;
            return '\0';
        }
        return st[top--];
    }
    int popint(){
        if(isempty())
        {
            cout<<"STACK IS EMPTY!!"<<endl;
            return '\0';
        }
        return st[top--];
    }

    char peek()
    {
        if(isempty())
        {
            cout<<"STACK IS EMPTY!!"<<endl;
            return '\0';
        }
        return st[top];
    }

    int peekint()
    {
        if(isempty())
        {
            cout<<"STACK IS EMPTY!!"<<endl;
            return '\0';
        }
        return st[top];
    }


    int precedence(char ch)
{
    if(ch=='^')
        return 4;
    else if(ch=='*' || ch=='/' || ch=='%')
        return 3;
    else if(ch=='+' || ch=='-')
        return 2;
    else return 1;
}

void conversion(char infix[20],char postfix[20])
{
    char ch;
    int j=-1;
    for(int i=0;infix[i]!='\0';i++)
    {
        ch=infix[i];
        if(isalnum(ch))
        {
            postfix[++j]=ch;
        }
        else if(ch=='(')
            push(ch);
        else if(ch==')')
        {
            while(!isempty()&&peek()!='(')
            {
                postfix[++j]=pop();
            }
            pop();
        }
        else
        {
            while(!isempty()&&precedence(ch)<=precedence(peek()))
            {
                postfix[++j]=pop();
            }
            push(ch);
        }
    }
    while (!isempty())
    {
        postfix[++j]=pop();
    }
    postfix[++j]='\0';
}

int evaluate(char postfix[20])
{
    int res,op1,op2;
    for(int i=0;postfix[i]!='\0';i++)
    {
        char ch=postfix[i];
        if(isdigit(ch))
            push(ch=ch -'0');
        else 
        {
            op2=popint();
            op1=popint();
            switch(ch)
            {
                case '+':
                    res=op1+op2;
                    break;
                case '-':
                    res=op1-op2;
                    break;
                case '*':
                    res=op1*op2;
                    break;
                case '/':
                    res=op1/op2;
                    break;
                case '^':
                    res = 1;
                    for (int i = 0; i < op2; i++)
                    {
                        res *= op1;
                    }
                    break;
                default:
                    cout<<"INVALID OPERATOR!"<<endl;
                    return -1;
            }
            push(res);
        }
    }
    return popint();
}
};

int main()
{
    stack s;
    char postfix[20];
    char infix[20];
    
    int choice,res;
    do{
        cout << "\nINFIX AND POSTFIX OPERATIONS:\n";
        cout << "1. ENTER EQUATION\n";
        cout << "2. CONVERT TO POSTFIX\n";
        cout << "3. EVALUATE AN EQUATION\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch(choice)
        {
            case 1:
            {
                cout<<"ENTER THE INFIX EXPRESSION: "<<endl;
                cin>>infix;
                break;
            }
            case 2:
            {
                s.conversion(infix,postfix);
                cout<<"POSTFIX EXPRESSION: "<<postfix;
                break;
            }
            case 3:
            {
                cout<<"ENTER THE INFIX EXPRESSION TO EVALUATE: "<<endl;
                cin>>infix;
                s.conversion(infix,postfix);
                cout<<"POSTFIX EXPRESSION: "<<postfix;
                res=s.evaluate(postfix);
                cout<<"ANSWER AFTER EVALUATION: "<<res<<endl;
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