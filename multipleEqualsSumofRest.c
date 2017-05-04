#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>

typedef struct Pair Pair;
struct Pair {
    long long first;
    long long snd;
};

long long sumorial(int n) {
	long long fac = (n*n + n)/2;
	return fac;
}

Pair** removNb(long long n, int* length) {
  Pair ** ansA = 0, ** ansB = 0;
  int llen = *length;
  
  long long sum, minSum, tmpSum; // the min Sum will be if you exclude n and n-1
  long long a, b;
  double rootSum;
  sum = sumorial (n); // get the complete sumorial
  minSum = sum - n*2+1;
  //rootSum = sqrtf(1.0*n/2 + sqrtf(1.0*n/2) - 1.0*n*2 + 1.0); 
  //printf("%f", rootSum);
  for (a = 1; a < sqrtl(minSum); a++) // choose a  //sqrt(minSum)
  {
      for (b = minSum/a; b < n; b++) // for each possible b
      {
          if (a * b == sum - a - b)
          {
              if (ansA == 0)
              {
                 ansA = malloc( ++llen * sizeof(*ansA) );
                 ansB = malloc( llen * sizeof(*ansB) );
              }
              else
              {
                 ansA = realloc(ansA, ++llen * sizeof (*ansA) );
                 ansB = realloc(ansB, llen * sizeof (*ansB) );
              }
              ansA[llen-1] = malloc(sizeof(Pair));
              ansA[llen-1]->first = a;
              ansA[llen-1]->snd = b;
              ansB[llen-1] = malloc(sizeof(Pair));
              ansB[llen-1]->first = b;
              ansB[llen-1]->snd = a;
          }
      }
  }
  ansA = realloc(ansA, 2*llen * sizeof (*ansA) );
  for (a = llen-1, b = llen; a >= 0; a--, b++)
      ansA[b] = ansB[a];
  *length = 2*llen;
  return ansA;
}

void dotest(long long n, char* sexpr) {
    int lg = 0;
    Pair** act = removNb(n, &lg);
    printf("N Test: %lld**\n", n);
    for (int i = 0; i < lg; i++)
    {
        printf("%lld    %lld\n", act[i]->first, act[i]->snd);
    }
    if (act != 0) {
        free(act); act = NULL;
    }
}

int main() {
    printf("mult\n");
    dotest(26, "{{15, 21}{21, 15}}");
    dotest(100 , "{}");
    dotest(37 , "{{21, 31}{31, 21}}");
    dotest(101 , "{{55, 91}{91, 55}}");
    dotest(101 , "{{55, 91}{91, 55}}");
    dotest(503 , "{{55, 91}{91, 55}}");
    //unsigned long long big = 677076 * 738480;
    //printf("big math: %lld", big);

    return 0;
}