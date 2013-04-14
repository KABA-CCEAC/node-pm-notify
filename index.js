var pm = require('bindings')('pm.node'),
	EventEmitter = require('events').EventEmitter;

var notify = new EventEmitter();

pm.registerNotifications(function(msg) {
	notify.emit(msg);
});

module.exports = notify;