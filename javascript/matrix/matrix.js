//
// This is only a SKELETON file for the 'Matrix' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Matrix {
  constructor(string) {
    this.string = string.split("\n");
  }

  get rows() {
    return this.string.reduce((acc, val) => {
      let elem = val.split(" ");
      for (let i in elem){
        elem[i] = parseInt(elem[i])
      }
      acc.push(elem);
      return acc;
    }, []);
  }

  get columns() {
    return this.string.reduce((acc, val) => {
      let elem = val.split(" ");
      for (let i in elem){
        if (!acc[i]) {
          acc.push([]);
        }
        acc[i].push(parseInt(elem[i]));
      }
      
      return acc;
    }, []);
  }
}