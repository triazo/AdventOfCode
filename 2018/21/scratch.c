#include <stdio.h>

unsigned int clip(unsigned int x) {
    return x & 16777215;
}

int main() {
    unsigned int mod = 0;
    unsigned int r = 1<<16;
    unsigned int lmod = 0;
    unsigned int lr = 0;
    unsigned int smod = 0;
    unsigned int sr = 0;
    unsigned long int i = 0;
    do {
        i++;
        if (i % 1000000 == 0) {
            printf("%ld \r", i);
            fflush(stdout);
        }

        r = mod | 1<<16;
        mod = 1505483;

        do {
            mod = clip(clip(mod + (r & 255)) * 65899);
            //printf("%d \n", mod);
            if (256 > r) break;
            r = r >> 8;
            /* unsigned int t1 = 0; */
            /* while (1) { */
            /*     unsigned int t2 = (t1 + 1) << 8; */
            /*     if (t2 > r) { */
            /*         r = t1; */
            /*         break; */
            /*     } */
            /*     t1++; */
            /* } */
        } while (1);



        if (smod == 0 && sr == 0) {
            smod = mod;
            sr = r;
        }
        if (mod == smod && sr == r) {
            printf("Last mod: %d\n", lmod);
            fflush(stdout);
        }
        lmod = mod;
        lr = r;
        // printf("check %d\n",mod);
        //fflush(stdout);
    } while (mod != 0);
}
