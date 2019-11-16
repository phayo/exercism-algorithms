#include "darts.h"
#include <math.h>

int score(coordinate_t position)
{
    // Initializing variable for score positions
    double outer = 10.0;
    double inner = 5.0;
    double bull_eye = 1.0;


    // calculating the actual resultant length (radii)
    double resultant = sqrt(pow(position.x, 2) + pow(position.y, 2));

    int score = 0;

    if (resultant <= bull_eye)
    {
        score = (int)outer;
    }
    else if (resultant <= inner)
    {
        score = (int)inner;
    }
    else if (resultant <= outer)
    {
        score = (int)bull_eye;
    }

    return score;
}
