#include "resistor_color_duo.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int colorCode(resistor_band_t color[]){
    return (color[0] * 10) + color[1];
}
