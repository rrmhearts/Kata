#include <stdio.h>

int main() {
	char* items[] = { "apple", "banana", "cherry" };
	for (int i = 0; i < 3; ++i) {
    		printf("%s\n", items[i]);
	}
	return 0;
}
