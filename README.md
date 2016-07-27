# lopy

`lopy` is a small program that allows you to install and manage dependencies locally and run programs using those local dependencies in Python. It is analagous to `npm` from Node.js in that it installs packages in your local directory, rather than globally, but otherwise works simiarly to `pip`. 

## Usage

Given a `requirements.txt` file, you can simply run

```
> lopy install
```

And it will install all packages in `requirements.txt` locally, by default in `.pip/`. To change the default directory, you can specify a directory within the `.lopyconfig` file (see section [Config](#config) below).

To run something, you have two options: `lopy run` and `lopy exec`. `lopy run` is shorthand for `lopy exec python`, which is useful when running a local script or starting a development server, but if you have to run an executable from a package, you will have to use `lopy exec`. In short:

```
# Run some executable called `do_something` from a local package
> lopy exec do_something
# Run the server.py
> lopy run server.py
```

## License

MIT
