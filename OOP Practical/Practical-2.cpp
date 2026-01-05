#include<iostream>
using namespace std;

class Person
{
    public:
    string name;
    int age;
    string address;
    static int personCount;

    //Default Constructor
    Person()
    {
        name="";
        age=0;
        address="";
        personCount++;
        cout<<"DEFAULT CONSTRUCTOR CALLED!!"<<endl;
    }

    //Parameterized Constructor
    Person(string n,int a,string add)
    {
        name=n;
        age=a;
        address=add;
        personCount++;
        cout<<"PARAMETERIZED CONSTRUCTOR CALLED!!"<<endl;
    }

    //Copy Constructor
    Person(Person &p)
    {
        name=p.name;
        age=p.age;
        address=p.address;
        cout<<"Copy constructor called!!!"<<endl;
    }
    void display() const {
        cout << "NAME: " << name << endl;
        cout << "AGE: " << age << endl;
        cout << "ADDRESS: " << address << endl;
    }

    ~Person()
    {
        cout<<"Person Destructor called!!"<<endl;
        personCount--;
    }

    static void counter()
    {
        cout << "Number of Person objects: " << personCount << endl;
    }

    friend void personaldisplay(const Person&p);
};
void personaldisplay(const Person&p)
    {
        cout<<"NAME: "<<p.name<<endl;
        cout<<"AGE: "<<p.age<<endl;
        cout<<"ADDRESS: "<<p.address<<endl;
    }
int Person::personCount = 0;

class Student:public Person
{
    public:
    int prn;
    string classname;
    string *division;
    string bloodgroup;
    Student()
    {
        prn=0;
        classname="";
        division=NULL;
        bloodgroup="";
    }

    Student(int p,string c,const string& d,string bg)
    {
        prn=p;
        classname=c;
        division=new string(d);
        bloodgroup=bg;
    }
    inline void checkAGE() {
        try {
            string licence;
            if (this->age < 18) {
                throw "STUDENT CANNOT DRIVE!!!";
            } else {
                cout << "ENTER THE LICENCE NUMBER: ";
                cin >> licence;
                cout << "LICENCE ENTERED: " << licence << endl;
            }
        }
        catch (const char* msg) {
            cout << "EXCEPTION: " << msg << endl;
        }
    }
    void display() const {
        Person::display();
        cout << "PRN: " << prn << endl;
        cout << "CLASS: " << classname << endl;
        cout << "DIVISION: " << *division << endl;
        cout << "BLOOD GROUP: " << bloodgroup << endl;
    }
    ~Student()
    {
        delete division;
    }
};

int main()
{
    Person p1("HRISHI",20,"PUNE");
    Person::counter();
    personaldisplay(p1);
    Student s1(40, "10th", "A", "O+");
    s1.age = 20;
    s1.name="HRISHI";
    s1.address="PUNE";
    s1.checkAGE();
    s1.display();
    return 0;
}