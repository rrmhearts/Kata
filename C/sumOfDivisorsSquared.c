#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

typedef struct Pair Pair;
struct Pair {
    long long first;
    long long snd;
};
long long sumOfSquaredDivisors(long long val)
{
  long long sum = 0;
  for (int i = 1; i <= val; i++)
  {
      if (val % i == 0)
        sum += i*i;
  }
  return sum;
}
int isPerfectSquare(long long sq)
{
  long long root = sqrtl(sq);
  return root*root == sq && sq > 0;
}
// fill length with the number of pairs in your array of pairs
Pair** listSquared(long long m, long long n, int* length) {
    struct Pair ** ans = 0;
    int llen = *length;
    long long sum;
    Pair newPair;

    for (long long i = m; i <= n; i++)
    {
        sum = sumOfSquaredDivisors(i);
        
        if (isPerfectSquare(sum) )
        {
            if (ans == 0)
               ans = malloc( ++llen * sizeof(*ans) );
            else
               ans = realloc(ans, ++llen * sizeof (*ans) );
            ans[llen-1] = malloc(sizeof(Pair));
            ans[llen-1]->first = i;
            ans[llen-1]->snd = sum;
        }
    }
    *length = llen;
    return ans;
}

void dotest(long long m, long long n, char* sexpr) {
    int lg = 0;
    Pair** act = listSquared(m, n, &lg);
    printf ("\n****  %llu to %llu ****\n", m, n);
    for (int i = 0; i < lg; i++)
    {
      printf("%llu,   %llu\n", act[i]->first, act[i]->snd);
    }
    if (act != 0) {
        //free(act); act = NULL;
    }
}

int main() {
    dotest(1, 250, "{{1, 1}{42, 2500}{246, 84100}}");
    dotest(42, 250, "{{42, 2500}{246, 84100}}");
    dotest(250, 500, "{{287, 84100}}");
    dotest(300, 600, "{}");
    dotest(40, 43, "{42, 2500}");

    return 0;
}