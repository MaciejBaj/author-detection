///<reference path="./dev-types.d.ts"/>
var redux_1 = require('redux');
var immutable_1 = require('immutable');
var redux_thunk_1 = require('redux-thunk');
var promise_middleware_1 = require('../middleware/promise-middleware');
var logger_1 = require('./logger');
var reducers_1 = require('../reducers');
var persistState = require('redux-localstorage');
function configureStore(initialState) {
    var store = redux_1.compose.apply(void 0, [_getMiddleware()].concat(_getEnhancers()))(redux_1.createStore)(reducers_1["default"], initialState);
    _enableHotLoader(store);
    return store;
}
function _getMiddleware() {
    var middleware = [
        promise_middleware_1["default"],
        redux_thunk_1["default"],
    ];
    if (__DEV__) {
        middleware = middleware.concat([logger_1["default"]]);
    }
    return redux_1.applyMiddleware.apply(void 0, middleware);
}
function _getEnhancers() {
    var enhancers = [
        persistState('session', _getStorageConfig()),
    ];
    if (__DEV__ && window.devToolsExtension) {
        enhancers = enhancers.concat([window.devToolsExtension()]);
    }
    return enhancers;
}
function _enableHotLoader(store) {
    if (__DEV__ && module.hot) {
        module.hot.accept('../reducers', function () {
            var nextRootReducer = require('../reducers');
            store.replaceReducer(nextRootReducer);
        });
    }
}
function _getStorageConfig() {
    return {
        key: 'react-redux-seed',
        serialize: function (store) {
            return store && store.session ?
                JSON.stringify(store.session.toJS()) : store;
        },
        deserialize: function (state) { return ({
            session: state ? immutable_1.fromJS(JSON.parse(state)) : immutable_1.fromJS({})
        }); }
    };
}
exports["default"] = configureStore;
//# sourceMappingURL=configure-store.js.map