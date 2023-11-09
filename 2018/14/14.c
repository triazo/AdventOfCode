#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SIZE 201811480

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Requires an argument\n");
        return 1;
    }

    char* rs = (char*)malloc(SIZE);
    memset(rs, 0, SIZE);
    unsigned int elf1 = 0;
    unsigned int elf2 = 1;

    rs[0] = 3;
    rs[1] = 7;

    unsigned int next = 2;
    for (unsigned i = 0; i < SIZE/2; ++i) {
        char nr = rs[elf1] + rs[elf2];
        rs[next] = nr / 10;
        next += rs[next]; // Either increment or don't
        /* if (*(unsigned int*)((unsigned long int)rs + next - 6) == 0x00050601 && */
        /*     *(unsigned short int*)((unsigned long int)rs + next - 2) == 0x0106) { */
        /*     printf("broke at %d\n", next-6); */
        /*     break; */
        /* } */
        rs[next] = nr % 10;
        next++;

        elf1 = (elf1 + rs[elf1] + 1) % next;
        elf2 = (elf2 + rs[elf2] + 1) % next;;
        /* for (unsigned j = 0; j < i; j++) { */
        /*     printf("%d", rs[j]); */
        /* } */
        /* printf("\n"); */
    }

    for (unsigned i = 0; i < next; ++i) {
        if (*(unsigned int*)((unsigned long int)rs + i - 6) == 0x00050601 &&
            *(unsigned short int*)((unsigned long int)rs + i - 2) == 0x0106) {
            printf("broke at %d\n", i-6);
            break;
        }
    }
}
