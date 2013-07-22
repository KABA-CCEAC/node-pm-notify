#include "pm.h"

NanCallback* notificationCallback;
bool isNotificationRegistered = false;

void Notify(char* msg) {
  if (isNotificationRegistered) {
    v8::Local<v8::Value> argv[1];
    argv[0] = v8::String::New(msg);
    notificationCallback->Call(1, argv);
  }
}

NAN_METHOD(RegisterNotifications) {
  NanScope();

  NanCallback* callback = NULL;

  if (args.Length() == 0)
  {
    return NanThrowError("First argument must be a function");
  }

  if (args.Length() == 1) 
  {
    // callback
    if(!args[0]->IsFunction()) 
    {
      return NanThrowError("First argument must be a function");
    }

    callback = new NanCallback(v8::Local<v8::Function>::Cast(args[0]));
  }

  notificationCallback = callback;
  isNotificationRegistered = true;

  NanReturnUndefined();
}

NAN_METHOD(StartMonitoring) {
  NanScope();

  Start();

  NanReturnUndefined();
}

NAN_METHOD(StopMonitoring) {
  NanScope();

  Stop();

  NanReturnUndefined();
}

extern "C" {
  void init (v8::Handle<v8::Object> target) 
  {
    NODE_SET_METHOD(target, "registerNotifications", RegisterNotifications);
    NODE_SET_METHOD(target, "startMonitoring", StartMonitoring);
    NODE_SET_METHOD(target, "stopMonitoring", StopMonitoring);
    InitPM();
  }
}

NODE_MODULE(pm, init);
