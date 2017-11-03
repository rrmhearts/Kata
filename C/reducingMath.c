#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long gcdi(long long x, long long y) {
   if (y == 0)
     return llabs(x);
   return gcdi(y, x % y);
}
long long lcmu(long long a, long long b) {
    return (llabs(a) / gcdi(a,b) ) * llabs(b);
}
long long som(long long a, long long b) {
    return a + b;
}
long long maxi(long long a, long long b) {
    return a < b ? b : a;
}
long long mini(long long a, long long b) {
    return a < b ? a : b;
}

typedef long long (*generic_func_t) (long long, long long);

// result will be freed
long long* operArray(generic_func_t f, long long* arr, int sz, long long init) {
    long long res = init;
    long long * ans = malloc(sz * sizeof(long long));
    for (int i = 0; i < sz; i++)
    {
      res = f(res, arr[i]);
      ans[i] = res;
    }
    return ans;
}

//long long* operArray(generic_func_t f, long long* arr, int sz, long long init);

void dotest(generic_func_t f, long long* dta, int sz, long long init, char *expr) {
    long long *act = operArray(f, dta, sz, init);
    //char* sact = array2StringLongLong(act, sz);
    //char *sdta = array2StringLongLong(dta, sz);
    //if(strcmp(sact, expr) != 0)
    //    printf("Error. Expected \n%s\n but got \n%s\n", expr, sact);
    for (int i=0; i < sz; i++)
        printf("%llu\n", act[i]);
    //free(sact); free(sdta); 
    free(act);
}

int main() {
    printf("Fixed test Gcdi\n");
    {
        long long dta[6] = { 18, 69, -90, -78, 65, 40 };
        char* sol = "18, 3, 3, 3, 1, 1";
        dotest(gcdi, dta, 6, dta[0], sol);
    }
    printf("Fixed test lcmu\n");
    {
        long long dta[6] = { 18, 69, -90, -78, 65, 40 };
        char* sol = "18, 414, 2070, 26910, 26910, 107640";
        dotest(lcmu, dta, 6, dta[0], sol);
    }
    printf("Fixed test maxi\n");
    {
        long long dta[6] = { 18, 69, -90, -78, 65, 40 };
        char* sol = "18, 69, 69, 69, 69, 69";
        dotest(maxi, dta, 6, dta[0], sol);
    }
}