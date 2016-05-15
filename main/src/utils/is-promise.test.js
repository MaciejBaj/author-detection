"use strict";
var is_promise_1 = require('./is-promise');
var assert = require('assert');
describe('isPromise', function () {
    it('should return true if a Promise is provided', function () {
        var promise = new Promise(function (resolve) { return resolve(true); });
        var payload = {
            promise: promise,
        };
        assert(is_promise_1.default(payload));
    });
    it('should return false if something that is not a Promise is provided', function () {
        var badPayload1 = { hello: 'world' };
        var badPayload2 = ['hello', 'world'];
        var badPayload3 = 'hello world';
        var badPayload4 = 'hello world';
        assert(!is_promise_1.default({ promise: badPayload1 }));
        assert(!is_promise_1.default({ promise: badPayload2 }));
        assert(!is_promise_1.default({ promise: badPayload3 }));
        assert(!is_promise_1.default({ promise: badPayload4 }));
    });
});
//# sourceMappingURL=is-promise.test.js.map