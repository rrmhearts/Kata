#include <iostream>
#include <string>

using namespace std;

class complex {
    double re, im;

public:
    complex(double re, double im) : re(re), im(im) { } // should be re{re}, im{re} according to Strousoup
    complex(double re) : re(re), im(0) { }
    complex() : re(0), im(0) { }
    // complex(complex &&) = default;
    // complex& operator=(complex&&) = default;
    // complex(complex&& other) noexcept : re(other.re), im(other.im) { 
    //     std::cout << "complex(complex&& other): move constructor" << std::endl;
    //     // THIS IS NOT NEEDED
    //     other.re = 0; // if object pointer, = nullptr
    //     other.im = 0;
    // }

    double real() const { return re; }
    double imag() const { return im; }

    void real(double d) { re=d; }
    void imag(double d) { im=d; }

    complex& operator = (complex &c) {
        cout << "complex& operator = (complex &c)" << endl;
        re = c.re;
        im = c.im;
        return *this;
    }

    complex& operator+= (complex &c) { // & not needed here?
        re += c.re;
        im += c.im;
        return *this;
    }

    complex& operator-= (complex c) { // no &
        re-=c.re;
        im-=c.im;
        return *this;
    }

    complex& operator*= (complex c) {
        // (ac-bd) + (ad+bc)i
        std::tie(re, im) = std::make_tuple(re*c.re - im*c.im, re*c.im + c.re*im);
        return *this;
    }

    complex& operator*= (double d) {
        re *= d;
        im *= d;
        return *this;
    }

    double norm() {
        return sqrt(re*re + im*im);
    }

    std::string to_string() {
        return std::to_string(re) + " + " + std::to_string(im) + "i";
    }

    // Grant access to the output stream operator
    friend std::ostream& operator<<(std::ostream& os, complex& p) {
        return os << p.to_string();
    }
};

complex operator + (complex c, complex other) {
    cout << "complex operator + (complex c, complex other)" << endl;
    return complex(c.real() + other.real(), c.imag() + other.imag());
}

complex operator * (complex c, complex other) {
    // (ac-bd) + (ad+bc)i
    return complex (
        other.real()*c.real() - c.imag()*other.imag(),
        c.real()*other.imag() + other.real()*c.imag()
    );
}

bool operator==(complex c1, complex c2) {
    return c1.real() == c2.real() && c1.imag() == c2.imag();
}

bool operator!=(complex c1, complex c2) {
    return !(c1 == c2);
}

double norm(complex c) {
    return sqrt(c.real()*c.real() + c.imag()*c.imag());
}

int main () {

    complex c1(1, 2);
    complex c2(2, 3);
    complex c3 = c1 + c2;
    std::cout << c3.to_string() << std::endl;
    complex mu = c2 * c1;
    std::cout << "c1: " << c1.to_string() << std::endl;
    std:cout << "c2: " << c2.to_string() << std::endl;
    c2 *= c1;
    std::cout << "c2 *= c1 : " << c2.to_string() << std::endl;
    std::cout << "mult: " << mu.to_string() << std::endl;

    complex tada {c1 + c2*c3};
    std::cout << tada.norm() << std::endl;
    return 0;
}