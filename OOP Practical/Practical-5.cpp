#include<iostream>
using namespace std;
template<typename T>
T sorting(T arr[],int n)
{
    cout<<"\nUNSORTED ARRAY: \n"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }

    int min;
    for(int i=0;i<n;i++)
    {
        min=i;
        for(int j=i+1;j<n;j++)
        {
            if(arr[j]<arr[min])
                min=j;
        }
        T temp;
        temp=arr[i];
        arr[i]=arr[min];
        arr[min]=temp;
    }

    cout<<"\nSORTED ARRAY IS AS FOLLOWS: \n"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
} 
int main()
{
    int n,choice;
    do
    {
        cout<<"\n***************MENU***************\n1.INTEGER ARRAY\n2.FLOAT ARRAY\n3.EXIT\n"<<endl;
        cout<<"ENTER YOUR CHOICE: "<<endl;
        cin>>choice;
        switch(choice)
        {
            case 1:{
                int arr[10];
                cout<<"ENTER THE INTEGER ARRAY SIZE: "<<endl;
                cin>>n;
                cout<<"ENTER ARRAY ELEMENTS: "<<endl;
                for(int i=0;i<n;i++)
                {
                    cout<<"ENTER ELEMENT: ";
                    cin>>arr[i];
                }
                sorting(arr,n);
                break;
            }
            case 2:
            {
                float arr[10];
                cout<<"ENTER THE FLOAT ARRAY SIZE: "<<endl;
                cin>>n;
                cout<<"ENTER ARRAY ELEMENTS: "<<endl;
                for(int i=0;i<n;i++)
                {
                    cout<<"ENTER ELEMENT: ";
                    cin>>arr[i];
                }
                sorting(arr,n);
                break;
            }
            case 3:{
                cout<<"EXITING....."<<endl;
                break;
            }
            default:{
                cout<<"INVALID INPUT!!!!"<<endl;
                break;
            }
        }
    } while(choice!=3);
    return 0;
}