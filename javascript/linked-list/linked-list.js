//
// This is only a SKELETON file for the 'Linked List' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class LinkedList {
  constructor() {
    this.list = [];
  }

  push(item) {
    this.list.push(item);
  }

  pop() {
    return this.list.pop();
  }

  shift() {
    return this.list.shift();
  }

  unshift(item) {
    this.list.unshift(item);
  }

  delete(item) {
    const index = this.list.indexOf(item);

    if (index >= 0) {
      this.list.splice(index, 1);
    }
  }

  count() {
    return this.list.length;
  }
}
