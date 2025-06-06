// lucky
#include <stdlib.h>
intmain() {
    int n = 10; // Number of random numbers to generate
    for (int i = 0; i < n; i++) {
        int random_number = rand() % 100; // Generate a random number between 0 and 99
        printf("%d\n", random_number); // Print the random number
    }
    return 0;
}