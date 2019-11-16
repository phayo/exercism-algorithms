//
// This is only a SKELETON file for the 'List - Ops' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class List {
  constructor(arrayOfList = []) {
    this.values = arrayOfList
    this.len = arrayOfList.length
  }

  append(list) {
    return new List([ ...this.values, ...list.values])
  }

  // concat(newList) {
    
  // }

  concat(newList){

    let currList = this.values.slice()

    for (let item of newList.values) {
      if (item) {
        if (item.values) {
          currList = [...currList, ...item.values]
        } else {
          currList = [...currList, item]
        }
      }
    }

    return new List(currList)
  }

  filter(arrFunc) {
    const newList = [];
    for (let item of this.values){
      if (arrFunc(item)){
        newList.push(item)
      }
    }
    return new List(newList)
  }

  map(mapFunc) {
    for (let i in this.values){
      this.values[i] = mapFunc(this.values[i])
    }

    return new List(this.values)
  }

  length() {
    return this.len;
  }

  foldl(reducer, init) {
    if(!init){
      init = this.values[0]
    }
    // console.log(this.values)
    let result = init
    for (let i = 0; i < this.len; i++){
      const item = this.values[i]
      result = reducer(result, item)
    }

    return result;
  }

  foldr(reducer, init) {
    const l = this.len;

    if(!init){
      init = this.values[l]
    }

    let result = init
    
    for (let i = 0; i < l; i++){
      let m = l - (i + 1)
      result = reducer(result, this.values[m])
    }

    return result;
  }

  reverse() {
    const tempArray = [ ...this.values ];
    const l = this.len;
    for (let i = 0; i < l; i++){
      let m = l - (i + 1)
      this.values[i] = tempArray[m]
    }
    return new List(this.values)
  }

  static isList(list){
    if (list.values && list.len){
        return true;
    }
    return false;
  }
}

const list1 = new List([1, 2]);
const list2 = new List([3]);
const list3 = new List([]);
const list4 = new List([4, 5, 6]);
const listOfLists = new List([list2, list3, list4])
console.log(list1.concat(list3).values)
console.log(List.isList(list1))