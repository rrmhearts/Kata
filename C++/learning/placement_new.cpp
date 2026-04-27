// C++ program to illustrate the placement new operator
#include<iostream>
using namespace std;

int main()
{
    cout << " E.g. 1 **************************************" << endl;
    // *********** Placement new in buffer **************//
    // buffer on stack
    unsigned char buf[sizeof(int)*2] ;

    // placement new in buf first 4 bytes 0-3
    int *pInt = new (buf) int(3);

    // starting from 4th byte 4-7
    int *qInt = new (buf + sizeof (int)) int(5);
    int *pBuf = (int*)(buf+0) ;
    int *qBuf = (int*) (buf + sizeof(int));
    cout << "Buff Addr             Int Addr" << endl;
    cout << pBuf <<"             " << pInt << endl;
    cout << qBuf <<"             " << qInt << endl;
    cout << "------------------------------" << endl;
    cout << "1st Int             2nd Int" << endl;
    cout << *pBuf << "                         "
         << *qBuf << endl;

    // *********** Change value in place **************//
    cout << "E.g. 2************************************************" << endl;
    // initial value of X
    int X = 10;

    cout << "Before placement new :" << endl;
    cout << "X : " << X << endl;
    cout << "&X : " << &X << endl;

    // Placement new changes the value of X to 100
    int *mem = new (&X) int(100);

    cout << "\nAfter placement new :" << endl;
    cout << "X : " << X << endl;
    cout << "mem : " << mem << endl;
    cout << "&X : " << &X << endl;

    return 0;
}