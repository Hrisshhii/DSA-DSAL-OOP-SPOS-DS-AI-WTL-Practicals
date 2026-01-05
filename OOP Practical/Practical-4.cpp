#include<iostream>
#include<fstream>
using namespace std;

class Student
{
    public:
    string name;
    int roll;
    int age;

    Student()
    {
        name="";
        roll=0;
        age=0;
    }

    void getdata()
    {
        cout<<"ENTER THE NAME OF STUDENT: "<<endl;
        getline(cin,name);
        cout<<"ENTER THE AGE OF STUDENT: "<<endl;
        cin>>age;
        cout<<"ENTER THE ROLL NUMBER OF THE STUDENT: "<<endl;
        cin>>roll;
    }

    void display()
    {
        cout<<"NAME: "<<name<<endl;
        cout<<"AGE: "<<age<<endl;
        cout<<"ROLL NUMBER: "<<roll<<endl;
    }
};

int main()
{
    Student s;
    s.getdata();
    ofstream fout;
    fout.open("Example.txt");
    if(fout.fail())
    {
        cout<<"ERROR OCCURED WHILE OPENING!!"<<endl;
        return 0;
    }
    fout.write((char*)&s,sizeof(s));
    cout<<"\nDATA ENTERED!!!!!!"<<endl;
    fout.close();

    ifstream fin;
    fin.open("Example.txt");
    if(fin.fail())
    {
        cout<<"ERROR OCCURED WHILE OPENING!!"<<endl;
        return 0;
    }
    cout<<"\nFILE OPENED TO DISPLAY DATA!!\n"<<endl;
    fin.read((char*)&s,sizeof(s));
    s.display();
    fin.close();

    return 0;
}