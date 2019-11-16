//
// This is only a SKELETON file for the 'Reverse String' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const reverseString = (string) => {
  if (string === ''){
    return '';
  }

  return string.split('').reverse().join('');
};


console.log(reverseString("Ebuka Obi"))