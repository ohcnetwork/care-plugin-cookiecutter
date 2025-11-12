# Installation

## Stable release

To install {{ cookiecutter.plugin_name }}, run this command in your terminal:

```sh
pip install {{ cookiecutter.plugin_name }}
```

## From source

The source files for {{ cookiecutter.plugin_name }} can be downloaded from the [Github repo](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}).

You can either clone the public repository:

```sh
git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}
```

Or download the [tarball](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}/tarball/master):

```sh
curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}/tarball/master
```

Once you have a copy of the source, you can install it with:

```sh
cd {{ cookiecutter.plugin_slug }}
pip install .
```
