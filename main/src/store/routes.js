"use strict";
var React = require('react');
var react_router_1 = require('react-router');
var app_1 = require('../containers/app');
var about_page_1 = require('../containers/about-page');
var counter_page_1 = require('../containers/counter-page');
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = (React.createElement(react_router_1.Route, {path: "/", component: app_1.default}, React.createElement(react_router_1.IndexRoute, {component: counter_page_1.default}), React.createElement(react_router_1.Route, {path: "about", component: about_page_1.default})));
//# sourceMappingURL=routes.js.map