#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// const char *ASCII_CHARS = "@%#*+=-:. ";  // Dark to light
// const int ASCII_LEN = 9; // strlen(ASCII_CHARS) - 1

const char *ASCII_CHARS = "$@B8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.. ";
// const char *ASCII_CHARS_rev = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[]2ES9d4VpOGbUAKXHm8RD#$0MNW&@";
const int ASCII_LEN = 70;

// Maps grayscale value (0–255) to ASCII character
char gray_to_ascii(unsigned char gray, int inverted) {
    int index = (int)((gray / 255.0) * ASCII_LEN + 0.5);
    if (inverted)
        index = ASCII_LEN - index;
    if (index > ASCII_LEN) index = ASCII_LEN;
    return ASCII_CHARS[index];
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s input_image output.txt -invert\n", argv[0]);
        return 1;
    }

    const char *input_filename = argv[1];
    const char *output_filename = argv[2];
    int inverted = 0;

    if (argc == 4 && strstr(argv[3], "invert") != NULL)
        inverted = 1;

    int width, height, channels;
    unsigned char *img = stbi_load(input_filename, &width, &height, &channels, 1); // Force grayscale

    if (!img) {
        fprintf(stderr, "Failed to load image: %s\n", input_filename);
        return 1;
    }

    FILE *out = fopen(output_filename, "w");
    if (!out) {
        fprintf(stderr, "Failed to open output file: %s\n", output_filename);
        stbi_image_free(img);
        return 1;
    }

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            unsigned char gray = img[y * width + x];
            fputc(gray_to_ascii(gray, inverted), out);
        }
        fputc('\n', out);
    }

    fclose(out);
    stbi_image_free(img);
    printf("ASCII art saved to %s\n", output_filename);
    return 0;
}

// gcc ascii_image.c -o ascii_image -lm
// ./ascii_image input.jpg output.txt -inverse
