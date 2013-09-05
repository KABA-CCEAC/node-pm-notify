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

	var started = true;

	notify.startMonitoring = function() {
		if (started) return;

		started = true;
		pm.startMonitoring();
	};

	notify.stopMonitoring = function() {
		if (!started) return;

		started = false;
		pm.stopMonitoring();
	};

	notify.version = index.version;
	global[index.name] = notify;

	module.exports = notify;
}