var index = require('./package.json');

if (global[index.name] && global[index.name].version === index.version) {
	module.exports = global[index.name];
} else {
	var pm = require('bindings')('pm.node'),
		EventEmitter = require('events').EventEmitter;

	var notify = new EventEmitter();

	notify.setMaxListeners(1000);

	pm.registerNotifications(function(msg) {
		notify.emit(msg);
	});

	notify.startMonitoring = pm.startMonitoring;
	notify.stopMonitoring = pm.stopMonitoring;

	notify.version = index.version;
	global[index.name] = notify;

	module.exports = notify;
}