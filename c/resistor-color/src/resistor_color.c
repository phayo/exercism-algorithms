#include "resistor_color.h"

int colorCode(resistor_band_t color){
    return color;
}
static resistor_band_t all_colors[10] = {BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY, WHITE};

resistor_band_t* colors(void)
{
    return all_colors;
}