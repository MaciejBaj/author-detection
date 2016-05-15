"use strict";
var React = require('react');
var ReactDOM = require('react-dom');
var react_redux_1 = require('react-redux');
var react_router_1 = require('react-router');
var react_router_redux_1 = require('react-router-redux');
var routes_1 = require('./store/routes');
var configure_store_1 = require('./store/configure-store');
//enable tap events
require('react-tap-event-plugin/src/injectTapEventPlugin')();
// Global styles
require('./styles/index.css');
var store = configure_store_1.default({});
var history = react_router_redux_1.syncHistoryWithStore(react_router_1.browserHistory, store);
//enable tap events
ReactDOM.render(React.createElement("div", null, React.createElement(react_redux_1.Provider, {store: store}, React.createElement(react_router_1.Router, {history: history}, routes_1.default))), document.getElementById('root'));
//# sourceMappingURL=index.js.map