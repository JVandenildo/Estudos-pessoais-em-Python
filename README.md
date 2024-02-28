# Studies In Python

Repository for Python algorithm/syntax testing.

## Summary

1. [Naming conventions for Python](#naming-conventions-for-python);
2. [Websites of interest](#websites-of-interest).

## Naming conventions for Python

> [!NOTE]
> The [PEP 8](https://peps.python.org/pep-0008) describes naming conventions and another similar stuff.

- Don't use single character "l", "I" or "O" as variable names;
- **Modules** should use short, all-lowercase names with underscore to separate words;
- **Python packages** should be short, all lowercase names (underscore discouraged);
- **Classes** should use CamelCase convention;
- **Type Variable** should normally use CameCase convention;
  - Preferring short names and with suffixes like `_co` or `_contra`;
- **Exceptions Names** should use CamelCase convention and the suffix `Error` if the exception is an error;
- **Function** should be lowercase with underscore to separate words;
- **Variable** should be lowercase with underscore to separate words;
- **Global Variable** should be lowercase with underscore to separate words;
- **Function** and **Method Arguments** always use `self` (in instance methods) and `cls` (in class methods) for the first argument;
- **Method** and **Instance variables** should be lowercase with underscore to separate words.
  - One leading underscore ofr non-public method and instance variable;
  - To avoid name classes with subclasses use two leading underscores to invoke Python's name mangling rules.
- **Constants** usually written in all capital letters with underscores separating words and defined on a module level.

There are more recommendations on PEP website, visit there for more details.

## Websites of interest

- [python.org](https://www.python.org/);
- [ipython.org](https://ipython.org/notebook.html);
- [The Story of Python, by Its Creator, Guido van Rossum](https://www.youtube.com/watch?v=J0Aq44Pze-w), YouTube video on Oracle Developers channel;
- [peps (Python Enhancement Proposal)](https://peps.python.org/).
