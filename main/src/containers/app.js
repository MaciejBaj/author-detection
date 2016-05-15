"use strict";
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var React = require('react');
var react_redux_1 = require('react-redux');
var material_ui_1 = require('material-ui');
var recognition_tab_1 = require('../components/recognition-tab');
var learning_tab_1 = require('../components/learning-tab');
function mapStateToProps(state) {
    return {
        router: state.router,
    };
}
function mapDispatchToProps(dispatch) {
    return {};
}
var App = (function (_super) {
    __extends(App, _super);
    function App() {
        _super.apply(this, arguments);
    }
    App.prototype.render = function () {
        var children = this.props.children;
        return (React.createElement("div", null, React.createElement(material_ui_1.AppBar, {className: "app-bar", title: "Characteristics recognition", iconElementLeft: React.createElement("p", null)}), React.createElement(material_ui_1.Tabs, null, React.createElement(material_ui_1.Tab, {label: "Recognition"}, React.createElement(recognition_tab_1.RecognitionTab, null)), React.createElement(material_ui_1.Tab, {label: "Learning"}, React.createElement(learning_tab_1.LearningTab, null)))));
    };
    ;
    return App;
}(React.Component));
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = react_redux_1.connect(mapStateToProps, mapDispatchToProps)(App);
//# sourceMappingURL=app.js.map