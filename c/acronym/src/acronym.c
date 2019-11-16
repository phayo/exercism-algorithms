#include "acronym.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

char *abbreviate(const char *phrase)
{
    if(phrase == NULL || !strcmp(phrase, "")){
        return NULL;
    }
    // declare array of individual words in phrase
    char words[20][20];

    int i, j, k, l;
    k = j = 0;

    for (i = 0, l = strlen(phrase); i < l; i++)
    {
        if (phrase[i] ==' ' || phrase[i] == '\0' || phrase[i] == '-')
        {
            words[j][k] = '\0';
            j++;
            k=0;
        }
        else
        {
            //printf("%c", phrase[i]);
            words[j][k] = toupper(phrase[i]);
            k++;
        }
    }
    //printf("\n");
    char * output = malloc(sizeof(char) * 15);
    for (int m = 0; m < j + 1; m++)
    {
        output[m] = words[m][0];
    }
    output[j+1] = '\0';
    return output;
}

// int main(void){
//     printf("%s\n", abbreviate("ruby on rails"));
// }