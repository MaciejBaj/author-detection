"use strict";
var index_1 = require('../constants/index');
function increment() {
    return {
        type: index_1.INCREMENT_COUNTER,
    };
}
exports.increment = increment;
function decrement() {
    return {
        type: index_1.DECREMENT_COUNTER,
    };
}
exports.decrement = decrement;
//# sourceMappingURL=counter.js.map