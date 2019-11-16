#include "isogram.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool is_isogram(const char phrase[])
{
    if (phrase == NULL){
        return false;
    }
    int l = strlen(phrase), j = 0;
    char unique[l];
    for (int i = 0; i < l; i++)
    {
        if (phrase[i] == ' ' || phrase[i] == '-')
        {
            continue;
        }
        else
        {
            //strchr() checks if a char exits in a string and return NULL if not and the string from that
            // point forward otherwise
            if (i == 0 || strchr(unique, tolower(phrase[i])) == NULL)
            {
                unique[j] = tolower(phrase[i]);
                j++;
            }
            else
            {
                return false;
            }
        }
    }
    return true;
}

// int main(void)
// {
//     char put[] = "accentor";
//     if (is_isogram(put))
//     {
//         printf("True\n");
//     }
//     else
//     {
//         printf("False\n");
//     }
// }