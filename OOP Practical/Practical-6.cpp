#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class student
{
    public:
    string name,dob,tele;
    int roll,age;
    student()
    {
        name="";
        dob="";
        tele="";
        roll=0;
        age=0;
    }

    void getdata()
    {
        cin.ignore();
        cout<<"ENTER THE NAME OF STUDENT: "<<endl;
        getline(cin,name);
        cout<<"ENTER THE AGE OF STUDENT: "<<endl;
        cin>>age;
        cout<<"ENTER THE DATE OF BIRTH OF STUDENT:(DD/MM/YYYY) "<<endl;
        cin>>dob;
        cout<<"ENTER THE TELEPHONE NUMBER OF STUDENT: "<<endl;
        cin>>tele;
        cout<<"ENTER THE ROLL NUMBER OF STUDENT: "<<endl;
        cin>>roll;
    }

    void display()
    {
        cout<<"\nNAME: "<<name<<endl;
        cout<<"ROLL NUMBER: "<<roll<<endl;
        cout<<"DATE OF BIRTH: "<<dob<<endl;
        cout<<"AGE: "<<age<<endl;
        cout<<"TELEPHONE NUMBER: \n"<<tele<<endl;
    }

    bool operator ==(const student& obj)
    {
        return roll==obj.roll;
    }
};

bool compare(student& s1,student& s2)
{
    return s1.roll<s2.roll;
}

int main()
{
    int choice,num;
    vector<student>v1;
    do{
        cout<<"\n***************MENU***************\n1.ENTER DATA\n2.DISPLAY DATA\n3.SORTING DATA\n4.SEARCHING DATA\n5.EXIT"<<endl;
        cout<<"ENTER YOUR CHOICE: "<<endl;
        cin>>choice;
        switch(choice)
        {
            case 1:
            {
                cout<<"ENTER THE NUMBER OF STUDENTS: "<<endl;
                cin>>num;
                cout<<"ENTER THE DATA OF STUDENT: "<<endl;
                for(int i=0;i<num;i++)
                {
                    student s;
                    s.getdata();
                    v1.push_back(s);
                }
                cout<<"\nDATA ADDED TO THE VECTOR!\n"<<endl;
                break;
            }
            case 2:
            {
                cout<<"\nAll the entries are as follows: \n"<<endl;
                for(int i=0;i<v1.size();i++)
                {
                    v1[i].display();
                }
                cout<<"\nTotal data in the vector is \n"<<v1.size()<<endl;
                break;
            }
            case 3:
            {
                student s;
                sort(v1.begin(),v1.end(),compare);
                cout<<"data sorted successfully!!!"<<endl;
                break;
            }
            case 4:
            {
                student s;
                cout<<"Enter the roll of the Student you want to find: "<<endl;
                cin>>s.roll;
                vector<student>::iterator it;
                it=find(v1.begin(),v1.end(),s);
                if(it==v1.end())
                    cout<<"Student with roll number "<<s.roll<<" not found in Database!!"<<endl;
                else{
                    cout<<"STUDENT FOUND: "<<endl;
                    it->display();
                }
                break;
            }
            case 5:
            {
                cout<<"EXITING THE PROGRAM.....................:)"<<endl;
                break;
            }
            default:
            {
                cout<<"INVALID INPUT!!!"<<endl;
                break;
            }
        }
    }while(choice!=5);
    return 0;
}