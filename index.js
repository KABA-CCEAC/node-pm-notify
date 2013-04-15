var pm = require('bindings')('pm.node'),
	EventEmitter = require('events').EventEmitter;

var notify = new EventEmitter();

pm.registerNotifications(function(msg) {
	notify.emit(msg);
});

notify.startMonitoring = pm.startMonitoring;
notify.stopMonitoring = pm.stopMonitoring;

module.exports = notify;