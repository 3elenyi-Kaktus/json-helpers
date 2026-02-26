# JSON 

### _by 3elenyi Kaktus_

Basically a collection of wrappers for simpler interactions with standard `json` library.

## Internal logic

Since not all objects can be represented as a JSON by default, module `make_jsonable.py` adds this possibility via binding json encoder to object's `__json__` method. It's a user responsibility to write implementation of this method anywhere needed. Simply `import` the module to the entrypoint file, from which the program starts.

Additionally, `toReadableJSON` is a method to write a human friendly version of JSON object.