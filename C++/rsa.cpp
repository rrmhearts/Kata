#include <iostream>
#include <cmath>

// Greatest Common Divisor
int gcd(int a, int b) {
    while (b != 0) {
        int tmp = b;
        b = a % b;
        a = tmp;
    }
    return a;
}

// Modular Exponentiation (base^exp % mod)
long long mod_exp(long long base, long long exp, long long mod) {
    long long result = 1;
    base = base % mod;

    while (exp > 0) {
        if (exp % 2 == 1)
            result = (result * base) % mod;

        exp = exp >> 1;
        base = (base * base) % mod;
    }
    return result;
}

// Extended Euclidean Algorithm to find modular inverse
int mod_inverse(int e, int phi) {
    int t = 0, newt = 1;
    int r = phi, newr = e;

    while (newr != 0) {
        int quotient = r / newr;
        int temp = newt;
        newt = t - quotient * newt;
        t = temp;

        temp = newr;
        newr = r - quotient * newr;
        r = temp;
    }

    if (r > 1) return -1; // e is not invertible
    if (t < 0) t += phi;
    return t;
}

// RSA Example
int main() {
    // Choose two primes (small for example only!)
    int p = 61;
    int q = 53;

    // Compute n and phi(n)
    int n = p * q;
    int phi = (p - 1) * (q - 1);

    // Choose e (public exponent)
    int e = 17;
    while (gcd(e, phi) != 1)
        ++e;

    // Compute d (private exponent)
    int d = mod_inverse(e, phi);
    if (d == -1) {
        std::cerr << "Modular inverse failed.\n";
        return 1;
    }

    std::cout << "Public key: (" << e << ", " << n << ")\n";
    std::cout << "Private key: (" << d << ", " << n << ")\n";

    // Message to encrypt
    int message = 65;
    std::cout << "Original Message: " << message << "\n";

    // Encrypt: c = m^e mod n
    long long ciphertext = mod_exp(message, e, n);
    std::cout << "Encrypted Message: " << ciphertext << "\n";

    // Decrypt: m = c^d mod n
    long long decrypted = mod_exp(ciphertext, d, n);
    std::cout << "Decrypted Message: " << decrypted << "\n";

    return 0;
}
