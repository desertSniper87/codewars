class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min.apply(Math, args);
  }
}

var s = new SmallestIntegerFinder();
console.log(s.findSmallestInt([1, 2, 3]));

