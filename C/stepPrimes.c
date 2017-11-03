typedef int bool;
#define true 1
#define false 0
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long* step(int g, long long m, long long n) {
  int offset = 2;
  int curr = 0;
  int match = 0;
  bool Prime = false;
  bool divisable = false;

  // Return null on bad args
  if (n <= m || g < 2 || m < 2)
    return 0;
  long long * answer = (long long *)malloc(2 * sizeof(long long));
  memset(answer, 0, 2 * sizeof(long long) );

  // g will never be odd, because Odd + Odd = Even, return 0,0
  if (g % 2 == 1)
    return answer;
    
  long long * primes = (long long*) malloc( (n-m) * sizeof(long long) );
  memset(primes, 0, (n-m) * sizeof(long long) );
  if (m % 2 == 0 ) // if even
    m++;
  for (long long firstV = m; firstV <= n; firstV+=offset )
  {
    Prime = true;
    
    // Remove basic primes, prevents second loop
    divisable = (firstV > 3 ? firstV % 3 == 0 : false)
             || (firstV > 5 ? firstV % 5 == 0 : false)
             || (firstV > 7 ? firstV % 7 == 0 : false)
             || (firstV > 11 ? firstV % 11 == 0 : false)
             || (firstV > 13 ? firstV % 13 == 0 : false)
             || (firstV > 17 ? firstV % 17 == 0 : false)
             || (firstV > 19 ? firstV % 19 == 0 : false)
             || (firstV > 23 ? firstV % 23 == 0 : false);


    if (!divisable)
    {
          for (long long div = 29; div*div <= firstV; div += 2)
          {
            if (firstV % div == 0)
            {
               Prime = false;
               break;
            }
          }

      if (Prime)
      {
        primes[curr] = firstV;
        curr ++;
        
        // Matching game for primes
        while (firstV != primes[match] + g && match < curr && primes[match]+g <= firstV)
        {
            match++;
        }
        // Found a match return it     // This comment is the prime gap solution
        if (firstV == primes[match] +g /* && firstV == primes[match+1]  */)
        {
          answer[0] = primes[match];
          answer[1] = firstV;
          return answer;
        }

      }
    }
  }
  return answer;
} // end step

int main () {
  long long * ans = step(2,2,50);
  printf("ans: %lld, %lld", ans[0], ans[1]);
  return 0;
}
