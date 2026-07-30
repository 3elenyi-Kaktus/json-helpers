# JSON helpers

#### _by 3elenyi Kaktus_

Basically a collection of wrappers for simpler interactions with standard `json` library.

# Usage concept

Since not all objects can be represented as a `JSON` by default, module `make_jsonable` adds this possibility via binding `JSON` encoder to object's `__json__` method. Additionally, it binds default serialization of `datetime` and `Path` objects. It's a user responsibility to write the real implementation of `__json__` method anywhere needed. Simply `import` the module to the entrypoint file, from which the program starts.

`toReadableJSON` is a method to write a human friendly version of JSON object.