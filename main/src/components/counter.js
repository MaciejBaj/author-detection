"use strict";
var React = require('react');
;
var Counter = function (_a) {
    var _b = _a.counter, counter = _b === void 0 ? 0 : _b, decrement = _a.decrement, increment = _a.increment;
    return (React.createElement("div", {className: "flex"}, React.createElement("div", {className: "flex-auto flex-center center"}, React.createElement("button", {style: styles.squareButton, className: "btn btn-primary bg-black", onClick: decrement}, "-")), React.createElement("div", {className: "flex-auto flex-center center h1"}, counter), React.createElement("div", {className: "flex-auto flex-center center"}, React.createElement("button", {style: styles.squareButton, className: "btn btn-primary", onClick: increment}, "+"))));
};
var styles = {
    squareButton: {
        width: 48,
        height: 48,
    },
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = Counter;
//# sourceMappingURL=counter.js.map