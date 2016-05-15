"use strict";
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var React = require('react');
var react_redux_1 = require('react-redux');
;
function mapStateToProps() {
    return {};
}
function mapDispatchToProps() {
    return {};
}
var AboutPage = (function (_super) {
    __extends(AboutPage, _super);
    function AboutPage() {
        _super.apply(this, arguments);
    }
    AboutPage.prototype.render = function () {
        return (React.createElement("h1", null, "About maci2o"));
    };
    return AboutPage;
}(React.Component));
;
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = react_redux_1.connect(mapStateToProps, mapDispatchToProps)(AboutPage);
//# sourceMappingURL=about-page.js.map