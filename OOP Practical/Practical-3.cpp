#include<iostream>
using namespace std;

class publication
{
    public:
    string title;
    float price;
    publication()
    {
        title="";
        price=0.0;
    }
    publication(string t,float pr)
    {
        title=t;
        price=pr;
    }

    virtual void display()
    {
        cout<<"TITLE: "<<title<<endl;
        cout<<"PRICE: "<<price<<"$"<<endl;
    }
};

class book:public publication
{
    public:
    int pages;
    book()
    {
        pages=0;
    }
    book(string t,float p,int pc)
    {
        title=t;
        price=p;
        pages=pc;
    }

    void display()
    {
        cout<<"TITLE OF BOOK: "<<title<<endl;
        cout<<"PAGE-COUNT: "<<pages<<endl;
        cout<<"PRICE: "<<price<<"$"<<endl;
    }
};
class tape:public publication
{
    public:
    float playtime;
    tape()
    {
        playtime=0.0;
    }
    tape(string t,float p,float pt)
    {
        title=t;
        price=p;
        playtime=pt;
    }

    void display()
    {
        cout<<"TITLE OF TAPE: "<<title<<endl;
        cout<<"PLAYTIME: "<<playtime<<" mins"<<endl;
        cout<<"PRICE: "<<price<<"$"<<endl;
    }
};

int main()
{
    try
    {
    string title;
    float price;
    int pages;
    float playtime;

    cout<<"ENTER THE TITLE OF THE BOOK: "<<endl;
    getline(cin,title);
    cout<<"ENTER THE PRICE OF THE BOOK: "<<endl;
    cin>>price;
    cout<<"ENTER THE NUMBER OF PAGES: "<<endl;
    cin>>pages;
    if(cin.fail())
    {
        throw "NOT VALID PAGES!!!";
    }
    book b(title,price,pages);

    cin.ignore();
    cout<<"ENTER THE TITLE OF THE TAPE: "<<endl;
    getline(cin,title);
    cout<<"ENTER THE PRICE OF THE TAPE: "<<endl;
    cin>>price;
    cout<<"ENTER THE PLAYTIME IN MINUTES: "<<endl;
    cin>>playtime;
    if(cin.fail())
    {
        throw "NOT VALID TIME!!!";
    }
    tape t(title,price,playtime);

    cout<<"\nBOOK INFORMATION: "<<endl;
    b.display();
    cout << "\nTape Information:" << endl;
    t.display();
    }
    catch(const char* msg)
    {
        cout<<"EXCEPTION CAUGHT: "<<msg<<endl;
        cout<<"RESETING TO ZERO VALUES!!! "<<endl;

        publication p;
        book b;
        tape t;

        cout << "\nBook Information (after reset):" << endl;
        b.display();
        cout << "\nTape Information (after reset):" << endl;
        t.display();
    }
    return 0;
}