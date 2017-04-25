// sz1: size of array1, sz2: size of array2, lg: size of the returned array
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
static int cmp(const void *p1, const void *p2){
    return strcmp(* (char * const *) p1, * (char * const *) p2);
}

char** inArray(char* array1[], int sz1, char* array2[], int sz2, int* lg) {
  // Sort first
  qsort(array1, sz1, sizeof(char *), cmp);
  
  // Answer storage
  char ** ans = malloc (sz1* sizeof (*ans) + (sz1*20*(sizeof (char) )) );
  char *pchar;
  int curr =0;
  
  // first string location
  char * data = (char*)&ans[sz1]; 
  for (int i = 0; i < sz1; i++)
  {
     ans[i] = data + i * 20;
  }
  //printf("\n");
  for (int j = 0; j < sz1; j++)
  {
    for (int i = 0; i < sz2; i++)
    {
        // Substring exists
        pchar = strstr(array2[i], array1[j]);
        // Copy substring to answer array
        if (pchar)
        {
          strcpy(ans[curr], array1[j]);
          curr++;
          break;
        }
     }
  }
  
  // Answer array size
  *lg = curr;
  return ans;
}

int main()
{
  char* arr1[3] = { "arp", "live", "strong" };
  char* arr2[5] = { "lively", "alive", "harp", "sharp", "armstrong" };
  
  int outSize;
  char ** outarray;
  outarray = inArray(arr1, 3, arr2, 5, &outSize);
  for (int i = 0; i < outSize; i++)
    printf("out : %s\n", outarray[i]);
  return 0;
}