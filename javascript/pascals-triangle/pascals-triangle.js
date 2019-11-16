//
// This is only a SKELETON file for the 'Pascals Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Triangle {
  constructor(base) {
    this.triangle = []
    for (let i = 0; i < base; i++){
      let step = this.steps(i)
      this.triangle.push(step)
    }
  }

  steps(step){
    let limit = step + 1
    let stepValues = []
    for (let i = 0; i < limit; i++){
      if (i === 0 || i === step){
        stepValues.push(1)
      }else{
        let value = this.triangle[step-1][i] + this.triangle[step-1][i-1]
        stepValues.push(value)
      }
    }
    return stepValues;
  }

  get lastRow() {
    return this.triangle[this.triangle.length - 1];
  }

  get rows() {
    return this.triangle;
  }
}