#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H


typedef enum
{
    BLACK,
    BROWN,
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    VIOLET,
    GREY,
    WHITE
}
resistor_band_t;


int colorCode(unsigned int color);

resistor_band_t* colors(void);

#endif
