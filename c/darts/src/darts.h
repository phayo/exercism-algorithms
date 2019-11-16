#ifndef DARTS_H
#define DARTS_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct coordinate {
  double x;
  double y;
} coordinate_t;

int score(coordinate_t position);

#endif
