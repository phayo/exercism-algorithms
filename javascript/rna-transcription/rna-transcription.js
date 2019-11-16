//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const key = {
  G: "C",
  C: "G",
  T: "A",
  A: "U"
};
export const toRna = dna => {
  let dNA = "";
  for (let i = 0; i < dna.length; i++) {
    dNA += key[dna[i]];
  }
  return dNA;
};
