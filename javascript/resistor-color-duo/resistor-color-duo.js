//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const colors = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white"
];

export const value = input => {
  const value = input.reduce((acc, color, ind) => {
    if (ind < 2) {
      return acc + colors.indexOf(color);
    }
    return acc;
  }, "");

  return parseInt(value);
};
