"use strict";
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var React = require('react');
var react_redux_1 = require('react-redux');
var counter_1 = require('../actions/counter');
var counter_2 = require('../components/counter');
function mapStateToProps(state) {
    return {
        counter: state.counter.get('count'),
    };
}
function mapDispatchToProps(dispatch) {
    return {
        increaseCounter: function () { return dispatch(counter_1.increment()); },
        decreaseCounter: function () { return dispatch(counter_1.decrement()); },
    };
}
var CounterPage = (function (_super) {
    __extends(CounterPage, _super);
    function CounterPage() {
        _super.apply(this, arguments);
    }
    CounterPage.prototype.render = function () {
        var _a = this.props, counter = _a.counter, increaseCounter = _a.increaseCounter, decreaseCounter = _a.decreaseCounter;
        return (React.createElement("div", null, React.createElement("h1", {className: "center"}, "Counter"), React.createElement(counter_2.default, {counter: counter, increment: increaseCounter, decrement: decreaseCounter})));
    };
    ;
    return CounterPage;
}(React.Component));
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = react_redux_1.connect(mapStateToProps, mapDispatchToProps)(CounterPage);
//# sourceMappingURL=counter-page.js.map