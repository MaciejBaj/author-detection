var rh = require('require-hacker');
['png',
    'jpg',
    'jpeg',
    'gif',
    'woff',
    'woff2',
    'ttf',
    'eot',
    'css',
    'svg',
].forEach(function (type) {
    rh.hook(type, function () { return "module.exports = \"\""; });
});
//# sourceMappingURL=entry.js.map