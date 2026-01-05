#include<iostream>
using namespace std;

class complex
{
    public:
    int real,imag;
    complex()
    {
        real=0;
        imag=0;
    }

    complex operator +(complex& obj)
    {
        complex temp;
        temp.real=real+obj.real;
        temp.imag=imag+obj.imag;
        return temp;
    }

    complex operator *(complex& obj)
    {
        complex temp;
        temp.real=real*obj.real-imag*obj.imag;
        temp.imag=real*obj.imag+imag*obj.real;
        return temp;
    }

    friend ostream &operator <<(ostream& out,complex& obj);
    friend istream &operator >>(istream& in,complex& obj);
};

istream &operator >>(istream& in,complex& obj)
{
    cout<<"ENTER REAL AND IMAGINARAY PART OF THE EQUATION: "<<endl;
    in>>obj.real>>obj.imag;
    return in;
}
ostream &operator <<(ostream& out,complex& obj)
{
    out<<obj.real<<"+"<<obj.imag<<"i"<<endl;
    return out;
}

int main()
{
    complex c1,c2,c3;
    cout<<"Enter the first complex number: "<<endl;
    cin>>c1;
    cout<<"Enter the second complex number: "<<endl;
    cin>>c2;
    c3=c1+c2;
    cout<<"ADDITION: "<<c3;
    c3=c1*c2;
    cout<<"MULTIPLICATION: "<<c3;
    return 0;
}