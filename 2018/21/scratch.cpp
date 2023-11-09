#include <stdio.h>
#include <set>

unsigned int clip(unsigned int x) {
    return x & 16777215;
}

unsigned int hash(unsigned int mod, unsigned int r) {
    return (r << 24 | mod);
}


int main() {
    unsigned int mod = 0;
    unsigned int r = 1<<16;
    unsigned int lmod = 0;
    unsigned int lr = 0;
    unsigned int smod = 0;
    unsigned int sr = 0;
    unsigned long int i = 0;

    std::set<unsigned int> stateset;

    stateset.insert(hash(mod, r));
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


        //printf("last r: %d\n", r);
        fflush(stdout);

        if (smod == 0 && sr == 0) {
            smod = mod;
            sr = r;
        }
        if (stateset.find(hash(mod, r)) != stateset.end()) {
            printf("Last mod: %d\n", lmod);
            fflush(stdout);
        }
        stateset.insert(hash(mod, r));

        lmod = mod;
        lr = r;
        // printf("check %d\n",mod);
        //fflush(stdout);
    } while (mod != 0);
}
