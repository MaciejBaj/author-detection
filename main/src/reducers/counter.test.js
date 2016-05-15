"use strict";
var assert = require('assert');
var fire_action_1 = require('../utils/fire-action');
var counter_1 = require('./counter');
var index_1 = require('../constants/index');
var immutable_1 = require('immutable');
var state = counter_1.default();
describe('counter reducer', function () {
    describe('inital state', function () {
        it('should be a Map', function () {
            assert.strictEqual(immutable_1.Map.isMap(state), true);
        });
    });
    describe('on INCREMENT_COUNTER', function () {
        it('should increment state.count', function () {
            var previousValue = state.get('count');
            state = fire_action_1.default(counter_1.default, state, index_1.INCREMENT_COUNTER);
            assert.strictEqual(state.get('count'), previousValue + 1);
        });
    });
    describe('on DECREMENT_COUNTER', function () {
        it('should decrement state.count', function () {
            var previousValue = state.get('count');
            state = fire_action_1.default(counter_1.default, state, index_1.DECREMENT_COUNTER);
            assert.strictEqual(state.get('count'), previousValue - 1);
        });
    });
});
//# sourceMappingURL=counter.test.js.map