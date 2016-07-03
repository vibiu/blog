## Markdown engine
### Install houdini
```
$ pip install houdini

// build dependent library
$ git clone 'https://github.com/zacharyvoase/houdini.git'
$ cd houdini
$ make

$ sudo cp libhoudini.so /usr/lib
$ sudo ldconfig     //Refresh the dynamic linker cache.
```
see [zacharyvoase/pyhoudini](https://github.com/zacharyvoase/pyhoudini)

### Install cffi
```
$ pip install cffi
```
see [CFFI Docs](https://cffi.readthedocs.io/en/latest/installation.html)

### Install misaka
need CFFI dependence
```
see [Misaka Docs](http://misaka.61924.nl/)
