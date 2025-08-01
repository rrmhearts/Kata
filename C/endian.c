#include <stdio.h>

int main() {
    unsigned int x = 0x12345678; // A 4-byte integer
    char *c = (char *)&x;       // Pointer to the first byte of x

    printf("Original integer: 0x%X\n", x);
    printf("Address of integer: %p\n", (void *)&x);

    // Print the individual bytes in memory
    printf("Bytes in memory (from lowest to highest address):\n");
    for (size_t i = 0; i < sizeof(x); i++) {
        printf("Byte %zu at address %p: 0x%02X\n", i, (void *)(c + i), (unsigned char)c[i]);
    }

    // Check the value of the first byte
    if (*c == 0x78) {
        printf("\nSystem is Little Endian.\n");
    } else if (*c == 0x12) {
        printf("\nSystem is Big Endian.\n");
    } else {
        printf("\nCould not determine endianness.\n");
    }

    return 0;
}