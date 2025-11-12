# Cookiecutter template for OHC Care Python Plugin Packages

This is a Cookiecutter template to create Python packages that can be used as plugins for the [OHC Care](https://github.com/ohcnetwork/care) ecosystem.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet:

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/ohcnetwork/care-plugin-cookiecutter.git
```

To install the generated plugin in care, navigate to care root directory and run:

```bash
pip install -e path/to/your/generated/plugin
```
After that you can visit `http://localhost:9000/api/care_plugin/hello` to see your plugin in action!


### Credits

- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
