#include<iostream>
using namespace std;

class icecream
{
    public:
    int prn;
    icecream *next;
    icecream():prn(0) , next(NULL){}

    icecream *adding(icecream *head,int roll)
    {
        icecream *p;
        p=new icecream;
        p->prn=roll;
        p->next=NULL;
        if(head==NULL){
            head=p;
            return head;
        }
        icecream *temp=head;
        while(temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->next=p;
        return head;
    }

    void display(icecream *head)
    {
        icecream *i;
        if(head==NULL)
        {
            cout<<"LIST IS EMPTY!!"<<endl;
        }
        cout<<"[";
        for(i=head;i->next!=NULL;i=i->next)
        {
            cout<<i->prn<<" ";
        }
        cout<<i->prn<<"]"<<endl;
    }

    icecream *intersection(icecream*van,icecream*but)
    {
        icecream *result=NULL;
        icecream *i,*j;
        for(i=van;i!=NULL;i=i->next)
        {
            for(j=but;j!=NULL;j=j->next)
            {
                if(i->prn==j->prn)
                {
                    result=adding(result,i->prn);
                }
            }
        }
        return result;
    }

    icecream *unionset(icecream*van,icecream*but)
    {
        icecream *result=NULL;
        icecream*i,*j;
        for(i=but;i!=NULL;i=i->next)
        {
            result=adding(result,i->prn);
        }
        for(i=van;i!=NULL;i=i->next)
        {
            icecream *temp=result;
            bool found=false;
            while(temp!=NULL){
                if(temp->prn==i->prn)
                {
                    found=true;
                    break;
                }
                temp=temp->next;
            }
            if(!found){
                result=adding(result,i->prn);
            }
        }
        return result;
    }

    int count(icecream* head)
    {
        icecream *i;
        int cnt=0;
        for(i=head;i!=NULL;i=i->next)
        {
            cnt++;
        }
        return cnt;
    }
};
int main()
{
    icecream *vanilla=NULL,*butterscotch=NULL;
    icecream flav;
    int roll,total;
    cout<<"ENTER TOTAL NUMBER OF STUDENTS: "<<endl;
    cin>>total;
    int choice;
    do{
        cout << "\n*******************MENU*******************\n"
            << "1. ADD MEMBER\n2. DISPLAY MEMBERS\n3. WHO LIKE BOTH\n4. WHO LIKE EITHER\n5. WHO LIKE NEITHER\n6. EXIT\n";
        cin >> choice;
        switch(choice)
        {
            case 1:
            {
                int ch;
                cout<<"WHICH FLAVOUR MEMBER TO ADD: \n1.VANILLA\n2.BUTTERSCOTCH"<<endl;
                cin>>ch;
                if(ch==1){
                    cout<<"ENTER THE PRN OF THE STUDENT WHO LIKES VANILLA: "<<endl;
                    cin>>roll;
                    vanilla=flav.adding(vanilla,roll);
                }
                else if(ch==2){
                    cout<<"ENTER THE PRN OF THE STUDENT WHO LIKES BUTTERSCOTCH: "<<endl;
                    cin>>roll;
                    butterscotch=flav.adding(butterscotch,roll);
                }
                else{
                    cout << "Invalid choice!" << endl;
                }
                break;
            }
            case 2:
            {
                int ch;
                cout<<"WHICH FLAVOUR MEMBER TO DISPLAY: \n1.VANILLA\n2.BUTTERSCOTCH"<<endl;
                cin>>ch;
                if(ch==1){
                    flav.display(vanilla);
                }
                else if(ch==2){
                    flav.display(butterscotch);
                }
                else{
                    cout << "Invalid choice!" << endl;
                }
                break;
            }
            case 3:
            {
                icecream* result;
                cout<<"STUDENT WHO LIKE BOTH: "<<endl;
                result=flav.intersection(vanilla,butterscotch);
                flav.display(result);
                break;
            }
            case 4:
            {
                icecream* result;
                cout<<"STUDENT WHO LIKE EITHER: "<<endl;
                result=flav.unionset(vanilla,butterscotch);
                flav.display(result);
                break;
            }
            case 5:
            {
                int count;
                icecream *result=flav.unionset(vanilla,butterscotch);
                count=flav.count(result);
                cout<<"NUMBER OF STUDENT WHO LIKE NEITHER: "<<total-count<<endl;
                break;
            }
            case 6: {
                cout << "Exiting the program. Goodbye!" << endl;
                break;
            }
            default:
                cout << "INVALID CHOICE. PLEASE TRY AGAIN!" << endl;
                break;
            }
    }while(choice!=6);
    return 0;
}