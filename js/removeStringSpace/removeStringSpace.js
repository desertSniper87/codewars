function noSpace(x){
    return_string = ""
    for (var i=0; i< x.length ; i++) {
        console.log(x[i]);
        if (x[i] !== " ") {
            return_string += x[i];
        }
    }

    console.log(return_string);
    return return_string;
}

var assert = require('assert');
assert.equal(noSpace('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB');
assert.equal(noSpace('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd');
assert.equal(noSpace('8aaaaa dddd r     '), '8aaaaaddddr');
