#include<iostream>
using namespace std;

class club
{
    public:
    int prn;
    string name;
    club *next;
    club()
    {
        prn=0;
        name="";
        next=NULL;
    }

    club *create()
    {
        club *head=NULL;
        club *p;
        int n;
        cout<<"ENTER THE NUMBER OF STUDENTS IN CLUB: "<<endl;
        cin>>n;
        for(int i=0;i<n-1;i++)
        {
            if(head==NULL)
            {
                head=new club;
                cout<<"ENTER THE NAME OF PRESIDENT: "<<endl;
                cin>>head->name;
                cout<<"ENTER THE PRN OF PRESIDENT: "<<endl;
                cin>>head->prn;
                head->next=NULL;
                p=head;
            }
            else 
            {
                p->next=new club;
                p=p->next;
                cout<<"ENTER THE NAME OF MEMBER: "<<endl;
                cin>>p->name;
                cout<<"ENTER THE PRN OF MEMBER: "<<endl;
                cin>>p->prn;
                p->next=NULL;
            }
        }
        p->next=new club;
        p=p->next;
        cout<<"ENTER THE NAME OF SECRETARY: "<<endl;
        cin>>p->name;
        cout<<"ENTER THE PRN OF SECRETARY: "<<endl;
        cin>>p->prn;
        p->next=NULL;
        return head;
    }

    void display(club *head)
    {
        cout<<"\nFIRST MEMBER IS THE PRESEIDENT WHILE LAST IS SECRETARY\n"<<endl;
        club *i;
        for(i=head;i->next!=NULL;i=i->next)
        {
            cout<<"[PRN: "<<i->prn<<" NAME: "<<i->name<<"]-> ";
        }
        cout<<"[PRN: "<<i->prn<<" NAME: "<<i->name<<"] ";
    }

    club *ad(club *head)
    {
        int ch;
        club *p,*i;
        cout<<"\nWHOM TO ADD!!\n1.PRESIDENT\n2.MEMBER\3.SECRETARY\n"<<endl;
        cin>>ch;
        if(ch==1)
        {
            p=new club;
            cout<<"ENTER THE NAME OF PRESIDENT: "<<endl;
            cin>>p->name;
            cout<<"ENTER THE PRN OF PRESIDENT: "<<endl;
            cin>>p->prn;
            p->next=head;
            head=p;
        }
        else if(ch==2)
        {
            int n;
            p=new club;
            cout<<"ENTER THE NAME OF MEMBER: "<<endl;
            cin>>p->name;
            cout<<"ENTER THE PRN OF MEMBER: "<<endl;
            cin>>p->prn;
            cout<<"ENTER THE PRN OF STUDENT AFTER WHOM YOU WANT TO ADD A NEW MEMBER: "<<endl;
            cin>>n;
            for(i=head;i->prn!=n;i=i->next);
            p->next=i->next;
            i->next=p;
        }
        else if(ch==3)
        {
            p=new club;
            cout<<"ENTER THE NAME OF SECRETARY: "<<endl;
            cin>>p->name;
            cout<<"ENTER THE PRN OF SECRETARY: "<<endl;
            cin>>p->prn;
            for(i=head;i->next!=NULL;i=i->next);
            i->next=p;
            p->next=NULL;
        }
        else{
            cout<<"INVALID INPUT!!!"<<endl;
        }
        return head;
    }

    club *del(club *head)
    {
        club *p,*i;
        int n;
        cout<<"WHOM TO DELETE: \n1.PRESIDENT\n2.MEMBER\3.SECRETARY\n"<<endl;
        cin>>n;
        if(n==1)
        {
            cout<<"NEXT PERSON WILL BECOME THE PRESIDENT!"<<endl;
            p=head;
            head=head->next;
            delete p;
        }
        else if(n==2)
        {
            int num;
            cout<<"ENTER THE PRN TO BE DELETED: "<<endl;
            cin>>num;
            for(i=head;i->next->prn!=num;i=i->next);
            p=i->next->next;
            delete i->next;
            i->next=p;
        }
        else if(n==3)
        {
            for(i=head;i->next->next=NULL;i=i->next);
            delete i->next;
            i->next=NULL;
        }
        else{
            cout<<"INVALID INPUT!!!"<<endl;
        }
        return head;
    }

    int counter(club *head)
    {
        int cnt=0;
        club *i;
        for(i=head;i!=NULL;i=i->next)
        {
            cnt++;
        }
        return cnt;
    }

    club *con(club *head1,club*head2)
    {
        club *p;
        for(p=head1;p->next!=NULL;p=p->next);
        p->next=head2;
        return head1;
    }
};
int main()
{
    club *head,*head1;
    club obj;
    int choice;
    do{
        cout<<"\n*********MENU*********\n1.CREATE A LIST\n2.DISPLAY MEMBERS\n3.ADD A MEMBER\n4.DELETE A MEMBER\n5.COUNT THE MEMBERS\n6.CONCATENATE TWO LISTS\n7.EXIT\n\nENTER YOUR CHOICE: "<<endl;
        cin>>choice;
        switch(choice)
        {
            case 1:
            {
                head=obj.create();
                break;
            }
            case 2:
            {
                obj.display(head);
                break;
            }
            case 3:
            {
                head=obj.ad(head);
                break;
            }
            case 4:
            {
                head=obj.del(head);
                break;
            }
            case 5:
            {
                int num;
                num=obj.counter(head);
                cout<<"TOTAL STUDENTS"<<num<<endl;
                break;
            }
            case 6:
            {
                cout<<"CREATING A LIST FOR SECOND CLASS: "<<endl;
                head1=obj.create();
                obj.display(head1);
                cout<<"\nCONCATENATING BOTH THE CLUBS: "<<endl;
                head=obj.con(head,head1);
                obj.display(head);
                break;
            }
            case 7:
            {
                cout<<"EXITING THE PROGRAM!!"<<endl;
                break;
            }
            default:
            {
                cout<<"INAVLID CHOICE!!"<<endl;
                break;
            }
        }
    }while(choice!=7);
    return 0;
}