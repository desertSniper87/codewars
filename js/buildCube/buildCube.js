function findNb(m) {
    // your code
    return (m*m*m);
}

var assert = require('assert');
assert.equal(findNb(4183059834009), 2022);
assert.equal(findNb(24723578342962), -1);
assert.equal(findNb(135440716410000), 4824);
assert.equal(findNb(40539911473216), 3568);
