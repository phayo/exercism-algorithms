//
// This is only a SKELETON file for the 'Grade School' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class GradeSchool {
  constructor() {
    this.db = {};
  }

  roster() {
    let clone = { ...this.db };
    const rost = Object.keys(clone).reduce((acc, key) => {
      acc[key] = clone[key].sort();
      return acc;
    }, {});
    return JSON.parse(JSON.stringify(rost));
  }

  add(name, grade) {
    if (!this.db.hasOwnProperty(grade)) {
      this.db[grade] = [];
    }
    this.db[grade].push(name);
  }

  grade(grade) {
    let clone = { ...this.db };
    const gradeRoster = clone[grade] ? clone[grade].sort() : [];
    return JSON.parse(JSON.stringify(gradeRoster));
  }
}
