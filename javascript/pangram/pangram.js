//
// This is only a SKELETON file for the 'Pangram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isPangram = text => {
  const letters = new Set("abcdefghijklmnopqrstuvwxyz");
  const string = new Set(text.toLowerCase().split(""));

  for (let elem of letters) {
    if (!string.has(elem)) {
      return false;
    }
  }
  return true;
};
