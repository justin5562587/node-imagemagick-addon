#include <node/node_api.h>
#include <node-addon-api/napi.h>

Napi::String Method(const Napi::CallbackInfo &info) {
    Napi::Env env = info.Env();
    return Napi::String::New(env, "World");
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    exports.Set(
            Napi::String::New(env, "HelloWorld"),
            Napi::Function::New<Method>(env)
    );
    return exports;
}

NODE_API_MODULE(j_image_addon_EXPORTS, Init)
