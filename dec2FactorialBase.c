#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long long ull;

char* dec2FactString(ull nb);
ull factString2Dec(char* str);

ull bases[37];
char factoradic[37] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

ull factoradic2Value(char fval)
{
    ull val;
    if ( fval >= 48 && fval < 58)
    {
        val = 0 + fval - 48;
    }
    else 
    {
        val = 10 + fval - 65;
    }
    printf("val: %llu\n", val);
    return val;
}

// result will be freed
char* dec2FactString(ull nb) {
    char * ans = malloc(1);
    ull i, coeff, HIGH = 0, ansPlace = 0;
    if (bases[1] != 1)
    { // setup bases
        bases[0] = 0;
        bases[1] = 1;
        for (i = 2; i <= 36; i++)
            bases[i] = bases[i-1]*i;
    }
    i = 36;
    while (i > 0)
    {
        coeff = 0;
        if ( nb >= bases[i])
        { // loop through values of base 36
            while ( nb >= (coeff+1)*bases[i] && coeff < i)
                coeff++;
            if (HIGH == 0)
            {
                HIGH = i;
                ans = realloc(ans, HIGH+2);
            }

            nb -= (coeff*bases[i]);
            ans[ansPlace] = factoradic[coeff];
            ansPlace++;
        }
        else if (ansPlace > 0)
        {
            ans[ansPlace] = factoradic[coeff];        
            ansPlace++;
        }
        
        i--;
    }
    ans[ansPlace++] = factoradic[0];
    ans[ansPlace] = 0;

    return ans;
}
ull factString2Dec(char* str) {
    int length = strlen(str);
    ull ans = 0;
    for (int i = 0; i < length; i++)
    {
        ans += factoradic2Value(str[i])*bases[length-1-i];
    }
    printf("ans; %llu\n", ans);
    return ans;
}



void dotest1(ull n, char* expr) {
    char* sact = dec2FactString(n);
    if (strcmp(sact, expr) != 0)
        printf("Error. Expected \n%s\n but got \n%s\n", expr, sact);
    else
      printf("%s,   %s\n", expr, sact);
    
}
void dotest2(char* s, ull n) {
    ull act = factString2Dec(s);
    if (act != n)
        printf("Error. Expected %llu\n but got %llu\n", n, act);
    else
        printf("%s,   %llu\n", n, act);
}
void dotest3(ull n, ull exp) {
    char* sact = dec2FactString(n);
    ull act = factString2Dec(sact);
    if (act != n)
        printf("Error. Expected %llu\n but got %llu\n", exp, act);
    else 
        printf("%llu,   %llu\n", exp, act);
}

int main () {
    printf("******** to Factorial\n");
    dotest1(2982, "4041000");
    dotest1(463, "341010");

    printf("******** from Factorial\n");
    dotest2("341010", 463);
    dotest2("65341010", 34303);
    
    printf("******** to Factorial and back\n");
    dotest3(999999999, 999999999);
    
    return 0;
}