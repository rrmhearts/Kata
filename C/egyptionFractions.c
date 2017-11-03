#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char* decompose(char* nrStr, char* drStr) {
  long long num = atof(nrStr);
  long long den = atof(drStr);
  double val = 1.0 * num / den;
  
  int curr_den = 2, curr_pos = 0;
  char * ans = malloc(1);
  ans[0] = 0;
  char denStr[50] = {0};

  if (val > 1)
  {
      sprintf(denStr, "%lld,", num/den);
      num -= (int)val * den;
      curr_pos += strlen(denStr);
      ans = realloc(ans, curr_pos+1 );
      strcat(ans, denStr);
  }
  printf("strlen:  %d\n", (int)strlen(denStr));
  while (num > 0)
  {
      val = 1.0*num/den;
      while (val < 1.0/curr_den)
        curr_den++;
      if (val >= 1.0/curr_den)
      {
        num *= curr_den;
        if (num >= den)
        {
            num -= den;
            sprintf(denStr, "1/%d,", curr_den);
            curr_pos += strlen(denStr);
            ans = realloc(ans, curr_pos+1 );
            printf("strlen:  %d\n", (int)strlen(denStr));

            strcat(ans, denStr);
        }
        den *= curr_den;
      }
  }
  ans[curr_pos-1] = '\0';
  return ans;
}

void dotest(char* u, char* v, char* expr) {
    char* sact = decompose(u, v);
    if(strcmp(sact, expr) != 0)
        printf("Error. Expected %s but got %s\n", expr, sact);
    printf("%s\n%s\n\n", sact, expr);
    free(sact); sact = NULL;
}

int main () {

    dotest("3", "4", "1/2,1/4");
    dotest("12","4", "3");
    dotest("4","5", "1/2,1/4,1/20");
    dotest("66","100", "1/2,1/7,1/59,1/5163,1/53307975");
    dotest("22","23", "1/2,1/3,1/9,1/83,1/34362");
    //dotest("99","101", "1/2,1/3,1/7,1/250,1/132563");
    return 0;
}