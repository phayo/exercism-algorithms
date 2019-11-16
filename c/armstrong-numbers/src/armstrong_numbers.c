#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include "armstrong_numbers.h"

bool isArmstrongNumber(int number)
{
    char numberStr[10];
    sprintf(numberStr, "%d", number);
    int len = strlen(numberStr);
    int sum = 0;
    for (int i = 0; i < len; i++)
    {
        int base = numberStr[i] - '0';
        long res = 1;
        int l = len;
        int k = 1;
        while (k <= l)
        {
            res *= base;
            k++;
        }
        sum += res;
    }
    if (sum == number)
    {
        return true;
    }
    return false;
}