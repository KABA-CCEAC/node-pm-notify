var pm = require('bindings')('pm.node'),
	EventEmitter = require('events').EventEmitter;

var notify = new EventEmitter();

pm.registerNotifications(function(msg) {
	notify.emit(msg);
});

module.exports = notify;

notify.on('wake', function() {
	console.log('wake');
});

notify.on('sleep', function() {
	console.log('sleep');
});