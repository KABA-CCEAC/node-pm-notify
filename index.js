var pm = require('bindings')('pm.node'),
	EventEmitter2 = require('eventemitter2').EventEmitter2;

var notify = new EventEmitter2({
	wildcard: true,
	delimiter: ':',
	maxListeners: 1000 // default would be 10!
});

pm.registerNotifications(function(msg) {
	notify.emit(msg);
});

module.exports = notify;