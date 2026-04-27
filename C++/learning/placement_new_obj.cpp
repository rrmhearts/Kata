// C++ program to illustrate using destructor for
// deleting memory allocated by placement new
#include<iostream>
#include<cstdlib>
#include<cmath>
using namespace std;

class Complex
{
private:
    double re_, im_;
public:
    // Constructor
    Complex(double re = 0, double im = 0): re_(re), im_(im)
    {
        cout << "Constructor : (" << re_
             << ", " << im_ << ")" << endl;
    }

    // Destructor
    ~Complex()
    {
        cout << "Destructor : (" << re_ << ", "
             << im_ << ")" << endl;
    }

    double normal()
    {
        return sqrt(re_*re_ + im_*im_);
    }

    void print()
    {
        cout << "|" << re_ <<" + " << im_
             << "i | = " << normal() << endl;
    }
};

// Driver code
int main()
{
    // buffer on stack
    unsigned char buf[100];

    Complex* pc = new Complex(4.2, 5.3);

    // array of two objects initialized with default values
    Complex* pd = new Complex[2];

    // using placement new
    Complex *pe = new (buf) Complex(2.6, 3.9);

    // use objects
    pc -> print();
    pd[0].print();
    pd[1].print();
    pe->print(); // on stack

    // Release objects
    // calls destructor and then release memory
    delete pc;

    // Calls the destructor for object pd[0]
    // and then release memory
    // and it does same for pd[1]
    delete [] pd;

    // No delete : Explicit call to Destructor.
    pe->~Complex(); // on stack

    // This can cause a funny error
    // debugger tries to free memory that does not exist in heap
    // delete pe; // don't do this

    return 0;
}