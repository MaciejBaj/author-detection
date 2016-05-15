var createLogger = require('redux-logger');
var immutable_to_js_1 = require('../utils/immutable-to-js');
var logger = createLogger({
    collapsed: true,
    stateTransformer: function (state) {
        return immutable_to_js_1["default"](state);
    },
    predicate: function (getState, _a) {
        var type = _a.type;
        return type !== 'redux-form/BLUR' &&
            type !== 'redux-form/CHANGE' &&
            type !== 'redux-form/FOCUS' &&
            type !== 'redux-form/TOUCH';
    }
});
exports["default"] = logger;
//# sourceMappingURL=logger.js.map