#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H

typedef enum resistor_band_t
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

typedef enum
{
    OHMS = 1,
    KILOOHMS = 1000
}
resistor_unit_t;

typedef struct resistor_value_t
{
    /* data */
    unsigned int value;
    resistor_unit_t unit;
}
resistor_value_t;


resistor_value_t colorCode(resistor_band_t color[]);

#endif
