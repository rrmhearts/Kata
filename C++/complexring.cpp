#include <iostream>
#include <vector>
#include <algorithm>
#include <initializer_list>

// The provided Complex class
class complex {
    double re, im;
public:
    complex(double re = 0, double im = 0) : re(re), im(im) { }
    
    double real() const { return re; }
    double imag() const { return im; }
    void real(double d) { re = d; }
    void imag(double d) { im = d; }

    // Basic arithmetic for the Ring operations
    complex operator+(const complex& other) const { return {re + other.re, im + other.im}; }
    complex operator-(const complex& other) const { return {re - other.re, im - other.im}; }
    complex operator*(const complex& other) const {
        return {re * other.re - im * other.im, re * other.im + im * other.re};
    }
    
    bool is_zero() const { return re == 0 && im == 0; }
};

// The Polynomial Ring Class C[x]
class ComplexPolynomial {
private:
    std::vector<complex> coeffs; // coeffs[i] is the coefficient of x^i

    void remove_leading_zeros() {
        while (coeffs.size() > 1 && coeffs.back().is_zero()) {
            coeffs.pop_back();
        }
    }

public:
    ComplexPolynomial(std::initializer_list<complex> list) : coeffs(list) {
        remove_leading_zeros();
    }

    ComplexPolynomial(std::vector<complex> c) : coeffs(std::move(c)) {
        remove_leading_zeros();
    }

    // Addition
    ComplexPolynomial operator+(const ComplexPolynomial& other) const {
        size_t n = std::max(coeffs.size(), other.coeffs.size());
        std::vector<complex> res(n);
        for (size_t i = 0; i < n; ++i) {
            complex a = (i < coeffs.size()) ? coeffs[i] : complex(0, 0);
            complex b = (i < other.coeffs.size()) ? other.coeffs[i] : complex(0, 0);
            res[i] = a + b;
        }
        return ComplexPolynomial(res);
    }

    // Subtraction (Additive Inverse)
    ComplexPolynomial operator-(const ComplexPolynomial& other) const {
        size_t n = std::max(coeffs.size(), other.coeffs.size());
        std::vector<complex> res(n);
        for (size_t i = 0; i < n; ++i) {
            complex a = (i < coeffs.size()) ? coeffs[i] : complex(0, 0);
            complex b = (i < other.coeffs.size()) ? other.coeffs[i] : complex(0, 0);
            res[i] = a - b;
        }
        return ComplexPolynomial(res);
    }

    // Multiplication
    ComplexPolynomial operator*(const ComplexPolynomial& other) const {
        size_t n = coeffs.size();
        size_t m = other.coeffs.size();
        std::vector<complex> res(n + m - 1, complex(0, 0));

        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                res[i + j] = res[i + j] + (coeffs[i] * other.coeffs[j]);
            }
        }
        return ComplexPolynomial(res);
    }

    void print() const {
        for (int i = coeffs.size() - 1; i >= 0; --i) {
            std::cout << "(" << coeffs[i].real() << " + " << coeffs[i].imag() << "i)";
            if (i > 0) std::cout << "x^" << i << " + ";
        }
        std::cout << std::endl;
    }
};

int main() {
    // Define some complex numbers
    complex c1(1, 1), c2(2, 0), c3(0, 1);

    // Create Polynomials
    // P1: (1+1i)x + 2
    ComplexPolynomial p1({complex(2, 0), complex(1, 1)});
    // P2: (0+1i)x + 1
    ComplexPolynomial p2({complex(1, 0), complex(0, 1)});

    std::cout << "P1: "; p1.print();
    std::cout << "P2: "; p2.print();

    // 1. Addition (Closure/Commutativity)
    std::cout << "\nAddition (P1 + P2): ";
    (p1 + p2).print();

    // 2. Subtraction (Additive Inverse)
    std::cout << "Subtraction (P1 - P2): ";
    (p1 - p2).print();

    // 3. Multiplication (Distributive/Associative)
    std::cout << "Multiplication (P1 * P2): ";
    (p1 * p2).print();

    return 0;
}