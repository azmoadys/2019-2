#include<iostream>
#include<string>
using namespace std;
int main(int argc, char** argv)
{
    string filename = "hello ";
    cout<< argv[1];
    filename += argv[1];
    cout <<"\n" << filename;
    cout <<"\n"<<"\n";  
    return 0;
}
