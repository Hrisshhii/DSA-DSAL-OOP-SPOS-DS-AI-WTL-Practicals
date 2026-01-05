#include<iostream>
using namespace std;

class Student
{
    public:
    string name;
    int prn;
    Student *next;
    Student* create();
    void display(Student *head);
    Student* ad(Student *head);
    Student* del(Student *head);
    int total(Student *head);
    void displayrev(Student* head);
    Student* con(Student *head1,Student *head2);
};

Student* Student::create()
{
    Student *head=NULL;
    Student *p;
    int n;
    cout<<"ENTER THE NUMBER OF MEMBERS: "<<endl;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        if(head==NULL)
        {
            head=new Student;
            cout<<"ENTER THE NAME OF THE STUDENT: "<<endl;
            cin>>head->name;
            cout<<"ENTER THE PRN OF THE STUDNENT: "<<endl;
            cin>>head->prn;
            head->next=NULL;
            p=head;
        }
        else{
            p->next=new Student;
            p=p->next;
            cout<<"ENTER THE NAME OF THE STUDENT: "<<endl;
            cin>>p->name;
            cout<<"ENTER THE PRN OF THE STUDNENT: "<<endl;
            cin>>p->prn;
            p->next=NULL;
        }
    }
    return head;
}

void Student::display(Student *head)
{
    Student *i;
    cout<<"FIRST OF THE LIST IS THE PRESIDENT AND LAST OF LIST IS THE SECRETARY: "<<endl;
    for(i=head;i->next!=NULL;i=i->next)
    {
        cout<<i->prn<<":"<<i->name<<"->";
    }
    cout<<i->prn<<":"<<i->name;
}

void Student::displayrev(Student *head)
{
    Student *i;
    if(head==NULL)
        return;
    displayrev(head->next);
    cout<<head->prn<<":"<<head->name<<" ";
}

Student* Student::ad(Student *head)
{
    int choice;
    Student *p;
    Student *i;
    cout<<"\nWHOM TO ADD: \n1.President\n2.Member\n3.Secretary\n"<<endl;
    cin>>choice;
        if(choice==1)
        {
            p=new Student;
            cout<<"Enter the New President name: "<<endl;
            cin>>p->name;
            cout<<"Enter the PRN of New President: "<<endl;
            cin>>p->prn;
            p->next=head;
            head=p;
        }
        else if(choice==2)
        {
            p=new Student;
            int temp;
            cout<<"Enter the New Member name: "<<endl;
            cin>>p->name;
            cout<<"Enter the PRN of New Member: "<<endl;
            cin>>p->prn;
            cout<<"ENTER THE NAME AFTER WHOM TO ADD THE NEW MEMBER: "<<endl;
            cin>>temp;
            for(i=head;i->prn!=temp;i=i->next);
            p->next=i->next;
            i->next=p;
        }
        else if(choice==3)
        {
            p=new Student;
            cout<<"Enter the New Sectretary name: "<<endl;
            cin>>p->name;
            cout<<"Enter the PRN of New Sectretary: "<<endl;
            cin>>p->prn;
            for(i=head;i->next!=NULL;i=i->next);
            i->next=p;
            p->next=NULL;
        }
        else
        {
            cout<<"INVALID CHOICE!!!!"<<endl;
        }
    
    return head;
}
Student* Student::del(Student *head)
{
    int choice;
    Student *i;
    cout<<"\nWHOM TO REMOVE: \n1.President\n2.Member\n3.Secretary\n"<<endl;
    cin>>choice;
    if(choice==1)
    {
        cout<<"NOTE: AFTER DELETION OF PRESIDENT THE NEXT MEMBER BECCOMES THE PRESIDENT!!!"<<endl;
        i=head;
        head=head->next;
        delete i;
    }
    else if(choice==2)
    {
        int temp;
        Student *tmp;
        cout<<"ENTER THE MEMBER's PRN TO BE DELETED: "<<endl;
        cin>>temp;
        for(i=head;i->next->prn!=temp;i=i->next);
        tmp=i->next;
        i->next=tmp->next;
        delete tmp;
    }
    else if(choice==3)
    {
        for(i=head;i->next->next!=NULL;i=i->next);
        delete i->next;
        i->next=NULL;
    }
    else{
        cout<<"Invalid CHOICE!!!!"<<endl;
    }
    return head;
}
int Student::total(Student *head)
{
    Student *i;
    int count=1;
    for(i=head;i->next!=NULL;i=i->next)
    {
        count++;
    }
    return count;
}

Student*Student::con(Student *head1,Student *head2)
{
    Student *i;
    for(i=head1;i->next!=NULL;i=i->next);
    i->next=head2;
    return head1;
}
int main()
{
    Student *head,*head1,*club;
    Student obj;
    int choice;
    do {
        cout << "\nClub Member Management System:\n";
        cout << "1. Create list\n";
        cout << "2. Display list\n";
        cout << "3. Display list in reverse\n";
        cout << "4. Add member\n";
        cout << "5. Delete member\n";
        cout << "6. Total members\n";
        cout << "7. Concatenate two classes!!!\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            head = obj.create();
            break;
        case 2:
            obj.display(head);
            break;
        case 3:
            cout << "List in reverse order: \n";
            obj.displayrev(head);
            cout << endl;
            break;
        case 4:
            head = obj.ad(head);
            break;
        case 5:
            head = obj.del(head);
            break;
        case 6:
            cout << "Total members in the club: " << obj.total(head) << endl;
            break;
        case 7:
            cout<<"\nCREATE CLUB OF SECOND CLASS: "<<endl;
            head1=obj.create();
            obj.display(head1);
            cout<<"\nCONCATENATE BOTH THE CLASSES: "<<endl;
            club=obj.con(head,head1);
            obj.display(club);
            break;
        case 8:
            cout << "Exiting..." << endl;
            break;
        default:
            cout << "Invalid choice!" << endl;
        }
    } while (choice != 8);
    return 0;
}