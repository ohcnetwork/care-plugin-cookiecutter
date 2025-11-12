# Prompts

When you create a package, you are prompted to enter these values.

## Templated Values

The following appear in various parts of your generated project:

- **full_name**: Your full name.
- **email**: Your email address.
- **github_username**: Your GitHub username.
- **plugin_name**: The name of your new Python package project. This is used in documentation and class names, only alphabets and spaces are allowed.
- **plugin_slug**: The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version of `plugin_name`. Note: your PyPI project links will use plugin_slug, so change those in the README afterwards.
- **plugin_short_description**: A 1-sentence description of what your Python package does.
- **first_version**: The starting version number of the package.
