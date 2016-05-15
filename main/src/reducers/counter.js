"use strict";
var index_1 = require('../constants/index');
var immutable_1 = require('immutable');
var INITIAL_STATE = immutable_1.fromJS({
    count: 0,
});
function counterReducer(state, action) {
    if (state === void 0) { state = INITIAL_STATE; }
    if (action === void 0) { action = { type: ' ' }; }
    switch (action.type) {
        case index_1.INCREMENT_COUNTER:
            return state.update('count', function (value) { return value + 1; });
        case index_1.DECREMENT_COUNTER:
            return state.update('count', function (value) { return value - 1; });
        case index_1.LOGOUT_USER:
            return state.merge(INITIAL_STATE);
        default:
            return state;
    }
}
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = counterReducer;
//# sourceMappingURL=counter.js.map