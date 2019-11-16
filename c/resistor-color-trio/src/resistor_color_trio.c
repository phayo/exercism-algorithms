#include "resistor_color_trio.h"
#include <stdio.h>
#include <math.h>

resistor_value_t colorCode(resistor_band_t color[]){
    resistor_value_t result;
    int duo = (color[0] * 10) + color[1];
    int zero = pow(10, color[2]);

    if ((duo * zero) % 1000 == 0){
        result.value = (duo * zero) / 1000;
        result.unit = KILOOHMS;
    }else{
        result.value = duo * zero;
        result.unit = OHMS;
    }

    return result;
}
