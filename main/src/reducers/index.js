"use strict";
var redux_1 = require('redux');
var react_router_redux_1 = require('react-router-redux');
var redux_form_1 = require('redux-form');
var counter_1 = require('./counter');
var rootReducer = redux_1.combineReducers({
    counter: counter_1.default,
    routing: react_router_redux_1.routerReducer,
    form: redux_form_1.reducer,
});
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = rootReducer;
//# sourceMappingURL=index.js.map