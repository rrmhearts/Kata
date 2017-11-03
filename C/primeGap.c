#include <stdlib.h>
#include <math.h>
#include <stdio.h>

long long* gap(int g, long long m, long long n) {
    long long * llptr = malloc(2*sizeof(long long));
    const long long sqroot = (long long)sqrt ((double) n);
    int prime[n + 1];
     
    for (int i = 0; i < n+1; i++)
      prime[i] = 1;

    prime[0] = 0;
    prime[1] = 0;
    long long first, j, i;
    for (i = 2; i <= sqroot; i++)
    {
        if (prime[i])
        {
            for (j = 2 * i; j <= n; j+=i)
                 prime[j] = 0; 
        }
    }
    for (j = m; j+g <= n; j++)
    {
        if (prime[j] && prime[j+g])
        {
          first = j;
          while (j+g <= n && !prime [j+1] ) j++;
          if (first+g == j+1)
          {
              llptr[0] = first;
              llptr[1] = first+g;
              return llptr;
          }
        }
    }
    llptr[0] = 0;
    llptr[1] = 0;
    return llptr;
}

int main()
{
  long long *ptr = gap(3, 2, 100);
  //printf("%lld   %lld\n", ptr[0], ptr[1]);
  
  ptr = gap (2,100,110);
  printf("%lld   %lld\n", ptr[0], ptr[1]);
  
  ptr = gap (4,100,110);
  printf("%lld   %lld\n", ptr[0], ptr[1]);
  
  ptr = gap (6,100,110);
  printf("%lld   %lld\n", ptr[0], ptr[1]);
  
  ptr = gap (8,300,400);
  printf("%lld   %lld\n", ptr[0], ptr[1]);

  //ptr = gap (10,900,999900);
  printf("%lld   %lld\n", ptr[0], ptr[1]);
  return 0;
}